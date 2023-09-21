import re
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Tuple, List, Set, Any, Callable, Dict
import logging
from tests.datastructure import ColumnMeta
from tests.util import dbutil

"""
채점을 위한 파일입니다. 수정하지 마세요.
"""
class ValidationRule:
    """This class validate value with given rules in order
        rules: rule list to apply validation in order(order is matter)
        Each rule return true if given value is valid
        * rules must not be empty
        """
    def __init__(self, rules: List[Callable[[Any], Tuple[bool, str]]]):
        self.rules = rules

    @abstractmethod
    def verify(self, v: Any) -> Tuple[bool, str]:
        pass


class OrValidationRule(ValidationRule):
    def verify(self, v: Any) -> Tuple[bool, str]:
        """Return true if any of rules return true, false otherwise"""
        err_strs = []
        for f in self.rules:
            r = f.verify(v) if isinstance(f, ValidationRule) else f(v)
            is_valid, err_str = r
            if is_valid:
                return (True, None)
            else:
                err_strs.append(err_str)
        return (False, f"""다음 중 하나는 참이어야 합니다. ({",".join(err_strs)})""")

    def __repr__(self):
        return f"""OR of multiple rules, Num of Rule {len(self.rules)}"""


class AndValidationRule(ValidationRule):
    def verify(self, v: Any) -> Tuple[bool, str]:
        """Return true if all rules return true, false otherwise"""
        for f in self.rules:
            r = f.verify(v) if isinstance(f, ValidationRule) else f(v)
            is_valid, err_str = r
            if not is_valid:
                return (False, err_str)
        return (True, None)

    def __repr__(self):
        return f"""AND of multiple rules, Num of Rule {len(self.rules)}"""


class HwScore(ABC):
    def __init__(self, max_score):
        self.max_score = max_score

    @abstractmethod
    def score(self) -> int:
        pass


class CreateTableProblem(HwScore):
    def __init__(self, max_score: int, table_name: str):
        super().__init__(max_score)
        self.table_name = table_name

    @abstractmethod
    def get_rules(self) -> List[Tuple[str, ValidationRule]]:
        pass

    def _get_enum_value_of_cols(self, enum_type: str) -> List[str]:
        enum = list(map(lambda a: a[0], dbutil.fetch_all(f"""
            select unnest(enum_range(null::{enum_type}))
        """, ())))
        enum.sort()
        return enum
        
    def _get_primary_key_columns(self) -> Set[str]:
        logging.info("Getting primary key columns")
        pk = dbutil.fetch_all("""
            SELECT c.column_name
            FROM information_schema.table_constraints tc 
            JOIN information_schema.constraint_column_usage AS ccu USING (constraint_schema, constraint_name) 
            JOIN information_schema.columns AS c ON c.table_schema = tc.constraint_schema
              AND tc.table_name = c.table_name AND ccu.column_name = c.column_name
            WHERE constraint_type = 'PRIMARY KEY' and tc.table_name = %s
        """, (self.table_name,))
        pk_set = {u for u, in pk}
        logging.info("Got primary key columns: %s", pk_set)
        return pk_set

    def _get_unique_columns(self) -> Set[str]:
        logging.info("Getting unique columns")
        unique = dbutil.fetch_all("""
            SELECT 
                column_name
            FROM 
                information_schema.table_constraints AS c
            JOIN information_schema.constraint_column_usage AS cc
            USING (table_schema, table_name, constraint_name)
            WHERE c.constraint_type = 'UNIQUE' and table_name = %s
        """, (self.table_name,))
        unique_set = {u for u, in unique}
        logging.info("Got unique columns: %s", unique_set)
        return unique_set

    def _is_table_exist(self) -> bool:
        is_exist, = dbutil.fetch_all("""
            select count(*) c from information_schema."tables" t where table_name = %s
        """, (self.table_name, ))[0]
        return is_exist == 1

    def _get_all_columns(self) -> Dict[str, ColumnMeta]:
        unique_set = self._get_unique_columns()

        logging.info("Getting all columns")
        columns = dbutil.fetch_all("""
            SELECT  
               lower(column_name), 
               case when is_nullable = 'YES' then true else false end as is_nullable,
               data_type,
               character_maximum_length,
               udt_name
            FROM 
               information_schema.columns
            WHERE 
               table_name = %s;
        """, (self.table_name,))
        columns_dict = {name: ColumnMeta(name, nullable, dtype, char_max_len, name in unique_set, udt_name)
                        for name, nullable, dtype, char_max_len, udt_name in columns}

        logging.info("Got columns: %s", columns_dict)
        return columns_dict

    def score(self) -> int:
        try:
            if not self._is_table_exist():
                logging.warning("Table %s not found", self.table_name)
                raise Exception("Table %s not found", self.table_name)
            logging.info("Table %s found, continue...", self.table_name)

        except Exception as e:
            logging.exception("Failed to check table %s exists", self.table_name)
            raise e
        try:
            # Validating table
            logging.info("Verifying table %s ...", self.table_name)
            columns_dict = self._get_all_columns()

        except Exception as e:
            logging.exception("Fail to get column info")
            raise e

        logging.info("Validating table definition")
        rules = self.get_rules()
        for col_name, rule in rules:
            if col_name not in columns_dict:
                logging.info("""No column "%s" in table %s""", col_name, self.table_name)
                raise Exception("""No column "%s" in table %s""", col_name, self.table_name)
            result, err_msg = rule.verify(columns_dict[col_name])
            if not result:
                logging.warning(err_msg)
                raise Exception(err_msg)
        return self.max_score


class ModifyRecordProblem(HwScore):
    def __init__(self, max_score: int, table_name: str, truncate=True):
        super().__init__(max_score)
        self.table_name = table_name
        self.truncate = truncate

    @abstractmethod
    def get_expected_data(self) -> list:
        pass

    @abstractmethod
    def order_by_col(self) -> str:
        pass

    def score(self) -> int:
        actual = dbutil.fetch_all(f"select * from {self.table_name} order by {self.order_by_col()}", ())
        expected = self.get_expected_data()

        logging.info("Validating data")

        # Remove padding spaces for char(n) column
        sanitized_actual = _sanitize_columns(actual)

        if sanitized_actual == expected:
            return self.max_score
        else:
            logging.warning("Insert 후 결과 값이 예상 값이 아닙니다. Expected %s, Actual %s", expected, actual)
            raise Exception(f"Insert 후 결과 값이 예상 값이 아닙니다. Expected {expected}, Actual {actual}")

def _sanitize_columns(values: list[Tuple]) -> Tuple:
    return [_sanitize_column_values(x) for x in values]

def _sanitize_column_values(value: Tuple) -> Tuple:
    return tuple([_sanitize_column_value(x) for x in value])

def _sanitize_column_value(value: Any) -> Any:
    if isinstance(value, str):
        newV = value.strip()
        if re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', newV):
            return datetime.strptime(newV, '%Y-%m-%d %H:%M:%S')
        else:
            return newV
    else:
        return value


class SelectRecordProblem(HwScore):
    def __init__(self, actual: Any, max_score: int):
        super().__init__(max_score)
        self.actual = actual

    @abstractmethod
    def get_expected_data(self) -> list:
        pass

    @abstractmethod
    def sort_actual(self, actual: Any) -> Any:
        pass

    def score(self) -> int:
        if isinstance(self.actual, list):
            self.sort_actual(self.actual)
            self.actual = _sanitize_columns(self.actual)

        expected = self.get_expected_data()


        logging.info("Validating data")
        if self.actual == expected:
            return self.max_score
        else:
            logging.warning("Query 결과 값이 예상 값이 아닙니다. Expected %s, Actual %s", expected, self.actual)
            raise Exception(f"Query 결과 값이 예상 값이 아닙니다. Expected {expected}, Actual {self.actual}")
