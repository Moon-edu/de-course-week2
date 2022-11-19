from score.traits import CreateTableProblem, ValidationRule, AndValidationRule, OrValidationRule
from typing import List, Tuple


class Q1Score(CreateTableProblem):
    def get_rules(self) -> List[Tuple[str, ValidationRule]]:
        return [
            ("emp_id", AndValidationRule([
                lambda c: (c.name == "emp_id", "Column 명은 반드시 emp_id여야 합니다."),
                lambda c: (not c.nullable, "emp_id는 null이 될 수 없습니다"),
                lambda c: (c.is_unique, "emp_id는 Table내에서 고유한 값을 가져야 합니다."),
                lambda c: ((c.dtype == "text" or (c.char_max_len and c.char_max_len >= 6)),
                           "emp_id는 고정 6자로 최소 6자 이상은 되어야 합니다."),
                lambda c: (c.dtype in ["character", "character varying", "text"],
                           """emp_id는 알파벳과 숫자의 조합이기때문에 char혹은 varchar 타입이어야 합니다. text도 정답으로 처리하지만 
                           6자리 문자를 표현하기 위해 권장되는 타입은 아닙니다.""")
            ])),
            ("gender", AndValidationRule([
                lambda c: (c.name == "gender", "Column 명은 반드시 gender여야 합니다."),
                lambda c: (not c.nullable, "gender는 null이 될 수 없습니다"),
                lambda c: (not c.is_unique, "gender는 Table내에서 고유한 값이 아닙니다."),
                OrValidationRule([
                    # If char / varchar
                    AndValidationRule([
                        lambda c: (c.dtype in ["character", "character varying", "text"], """
                            gender column은 Male, Female, Others를 표현하기 위해 최소 6자 길이의 char 혹은 varchar가 되어야 합니다.
                            text도 정답으로 처리하지만 6자리 문자를 표현하기 위해 권장되는 타입은 아닙니다.
                        """),
                        lambda c: ((c.dtype == "text" or (c.char_max_len and c.char_max_len >= 6)), """
                            gender column은 Male, Female, Others를 표현하기 위해 최소 6자 길이의 char 혹은 varchar가 되어야 합니다.
                            text도 정답으로 처리하지만 6자리 문자를 표현하기 위해 권장되는 타입은 아닙니다.
                        """),
                    ]),
                    # If Enum type
                    AndValidationRule([
                        lambda c: (c.dtype == "user-defined", "gender는 enum타입일 수 있습니다"),
                        lambda c: (self._get_enum_value_of_cols(c.udt_name) == ["Female", "Male", "Others"],
                                   """gender column이 enum일 경우 Female, Male, Others만 허용해야 합니다. 대소문자도 제대로 맞추어야 합니다.""")
                    ])
                ])
            ])),
            ("name", AndValidationRule([
                lambda c: (c.name == "name", "Column 명은 반드시 name여야 합니다."),
                lambda c: (not c.nullable, "name는 null이 될 수 없습니다"),
                lambda c: (not c.is_unique, "name는 Table내에서 고유한 값이 아닙니다"),
                lambda c: ((c.dtype == "text" or (c.char_max_len and c.char_max_len >= 20)), "name는 최소 20자 이상을 허용해야 합니다."),
                lambda c: (c.dtype in ["character", "character varying", "text"],
                           """name는 char혹은 varchar 타입이어야 합니다. text도 정답으로 처리하지만 
                           20자리 문자를 표현하기 위해 권장되는 타입은 아닙니다.""")
            ])),
            ("address", AndValidationRule([
                lambda c: (c.name == "address", "Column 명은 반드시 address여야 합니다."),
                lambda c: (c.nullable, "address는 null이 될 수 있습니다"),
                lambda c: (not c.is_unique, "address는 Table내에서 고유한 값이 아닙니다"),
                lambda c: ((c.dtype == "text" or (c.char_max_len and c.char_max_len >= 100)), "address는 최소 100자 이상을 허용해야 합니다."),
                lambda c: (c.dtype in ["character", "character varying", "text"],
                           """address는 char혹은 varchar 타입이어야 합니다. text도 정답으로 처리하지만 
                           100자리 문자를 표현하기 위해 권장되는 타입은 아닙니다.""")
            ])),
            ("department", AndValidationRule([
                lambda c: (c.name == "department", "Column 명은 반드시 department여야 합니다."),
                lambda c: (not c.is_unique, "department는 Table내에서 고유한 값이 아닙니다"),
                lambda c: (c.nullable, "department는 null이 될 수 있습니다"),
                lambda c: (c.dtype in ["integer", "smallint", "bigint"],
                           """department는 int혹은 smallint 타입이어야 합니다. bigint도 정답으로 처리하지만 
                           최대 100을 표현하기 위해 지나치게 큰 데이터 타입입니다.""")
            ])),
            ("manager", AndValidationRule([
                lambda c: (c.name == "manager", "Column 명은 반드시 manager여야 합니다."),
                lambda c: (c.nullable, "manager는 null이 될 수 있습니다"),
                lambda c: (not c.is_unique, "manager는 Table내에서 고유한 값이 아닙니다"),
                lambda c: ((c.dtype == "text" or (c.char_max_len and c.char_max_len >= 6)), "manager는 고정 6자로 최소 6자 이상은 되어야 합니다."),
                lambda c: (c.dtype in ["character", "character varying", "text"],
                           """manager는 알파벳과 숫자의 조합이기때문에 char혹은 varchar 타입이어야 합니다. text도 정답으로 처리하지만 
                           6자리 문자를 표현하기 위해 권장되는 타입은 아닙니다.""")
            ])),
            ("age", AndValidationRule([
                lambda c: (c.name == "age", "Column 명은 반드시 age여야 합니다."),
                lambda c: (not c.is_unique, "age는 Table내에서 고유한 값이 아닙니다"),
                lambda c: (not c.nullable, "age는 null이 될 수 없습니다"),
                lambda c: (c.dtype in ["integer", "smallint", "bigint"],
                           """age는 int혹은 smallint 타입이어야 합니다. bigint도 정답으로 처리하지만 
                           나이를 표현하기 위해 지나치게 큰 데이터 타입입니다.""")
            ])),
            ("position", AndValidationRule([
                lambda c: (c.name == "position", "Column 명은 반드시 positions여야 합니다."),
                lambda c: (c.nullable, "position는 null이 될 수 있습니다"),
                lambda c: (not c.is_unique, "position는 Table내에서 고유한 값이 아닙니다"),
                lambda c: ((c.dtype == "text" or (c.char_max_len and c.char_max_len >= 30)), "position는 최소 30자 이상을 허용해야 합니다."),
                lambda c: (c.dtype in ["character", "character varying", "text"],
                           """position는 char혹은 varchar 타입이어야 합니다. text도 정답으로 처리하지만 
                           30자리 문자를 표현하기 위해 권장되는 타입은 아닙니다.""")
            ]))
        ]


