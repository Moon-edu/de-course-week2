from abc import ABC, abstractmethod
from typing import Tuple, List, Set, Any, Callable, Dict
import logging
from datastructure import ColumnMeta
from util import dbutil


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
        for f in self.rules:
            r = f.verify(v) if isinstance(f, ValidationRule) else f(v)
            is_valid, err_str = r
            if is_valid:
                return (True, None)
        return (False, err_str)

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
    def __init__(self, filename, max_score):
        self.filename = filename
        self.max_score = max_score

    def _read_query(self) -> str:
        with open(f"homework/{self.filename}.sql", "r") as f:
            return f.read().strip()

    @abstractmethod
    def score(self) -> int:
        pass


class CreateTableProblem(HwScore):
    def __init__(self, filename: str, max_score: int, table_name: str):
        super().__init__(filename, max_score)
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
    def __init__(self, filename: str, max_score: int, table_name: str, truncate=True):
        super().__init__(filename, max_score)
        self.table_name = table_name
        self.truncate = truncate

    @abstractmethod
    def get_expected_data(self) -> list:
        pass

    @abstractmethod
    def order_by_col(self) -> str:
        pass

    def score(self) -> int:
        if self.truncate:
            try:
                dbutil.execute_sql(f"TRUNCATE table {self.table_name}")
            except Exception:
                logging.exception(f"Can't truncate table {self.table_name}")
                raise Exception(f"Can't truncate table {self.table_name}")
        try:
            logging.info("Reading query file from %s", self.filename)
            query = self._read_query()
            if not query:
                logging.warning("Query file %s is empty", self.filename)
                raise Exception(f"Query file {self.filename} is empty")
        except Exception:
            logging.exception("Failed to read query file %s", self.filename)
            raise Exception(f"Failed to read query file {self.filename}")
        try:
            logging.info("Executing query in file %s. query: %s", self.filename, query)
            dbutil.execute_sql(query)

            logging.info("Executed query: %s", query)
        except Exception:
            logging.exception("Failed to execute query %s in file %s", query, self.filename)
            raise Exception(f"Failed to execute query {query} in file {self.filename}")

        actual = dbutil.fetch_all(f"select * from {self.table_name} order by {self.order_by_col()}", ())
        expected = self.get_expected_data()

        logging.info("Validating data")
        if actual == expected:
            return self.max_score
        else:
            logging.warning("Insert 후 결과 값이 예상 값이 아닙니다. Expected %s, Actual %s", expected, actual)
            raise Exception(f"Insert 후 결과 값이 예상 값이 아닙니다. Expected {expected}, Actual {actual}")


class SelectRecordProblem(HwScore):
    def __init__(self, filename: str, max_score: int):
        super().__init__(filename, max_score)

    @abstractmethod
    def get_expected_data(self) -> list:
        pass

    @abstractmethod
    def sort_actual(self, actual: Any) -> Any:
        pass
    def score(self) -> int:
        try:
            logging.info("Reading query file from %s", self.filename)
            query = self._read_query()
            if not query:
                logging.warning("Query file %s is empty", self.filename)
                return 0
        except Exception:
            logging.exception("Failed to read query file %s", self.filename)
            return 0
        try:
            logging.info("Executing query in file %s. query: %s", self.filename, query)
            actual = dbutil.fetch_all(query, ())
            actual_sorted = self.sort_actual(actual)

            logging.info("Executed query: %s", query)
        except Exception:
            logging.exception("Failed to execute query %s in file %s", query, self.filename)
            return 0

        expected = self.get_expected_data()

        logging.info("Validating data")
        if actual_sorted == expected:
            return self.max_score
        else:
            logging.warning("Query 결과 값이 예상 값이 아닙니다. Expected %s, Actual %s", expected, actual)
            return 0
