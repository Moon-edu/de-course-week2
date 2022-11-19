from score.traits import CreateTableProblem, InsertRecordProblem, ValidationRule, AndValidationRule, OrValidationRule
from typing import List, Tuple
from datetime import datetime


class Q1Score(CreateTableProblem):
    def __init__(self):
        super().__init("q1_create_employee_table", 10, "employee")

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


class Q2Score(InsertRecordProblem):
    def __init__(self):
        super().__init__("q2_insert_employee_table", 5, "employee")

    def order_by_col(self):
        return "emp_id"

    def get_expected_data(self) -> list:
        return [
            ("A00001", "Male", "Moon", "10-199, Gang-nam, Seoul", 1, "C00001", 30, "Senior engineer"),
            ("A08771", "Others", "Peach", "203-3, Guro, Seoul", 1, "C00001", 26, "Junior engineer"),
            ("B00100", "Female", "Sun", "587/8, Gwan-ak, Seoul", 2, "B00102", 25, "Associate marketer"),
            ("B00102", "Female", "Ran", "290-10, Gwanghwamun, Seoul", 2, "C00000", 45, "Director"),
            ("C00000", "Male", "K", "1010, Sung-soo, Seoul", None, None, 51, "CEO"),
            ("C00001", "Male", "Lion", "53-3, Namyang-ju, Gyonghi", 1, "C00000", 55, "CTO"),
            ("C00002", "Others", "Cindy", "100, Jong-ro, Seoul", 3, "C00000", 52, "Director"),
            ("C00129", "Male", "Alex", "20-331, Bundang, Gyonggi", 3, "C00002", 40, "Director")
        ]

class Q3Score(CreateTableProblem):
    def __init__(self):
        super().__init__("q3_create_visit_log_table", 10, "visit_log")

    def get_rules(self) -> List[Tuple[str, ValidationRule]]:
        return [
            ("visitor", AndValidationRule([
                lambda c: (c.name == "visitor", "Column 명은 반드시 visitor여야 합니다."),
                lambda c: (c.nullable, "visitor는 null이 될 수 있습니다"),
                lambda c: (not c.is_unique, "visitor는 Table내에서 고유한 값이 아닙니다."),
                lambda c: ((c.dtype == "text" or (c.char_max_len and c.char_max_len >= 6)),
                           "visitor는 고정 6자로 최소 6자 이상은 되어야 합니다."),
                lambda c: (c.dtype in ["character", "character varying", "text"],
                           """visitor는 직원 ID이기 떄문에 char혹은 varchar 타입이어야 합니다. text도 정답으로 처리하지만 
                           6자리 문자를 표현하기 위해 권장되는 타입은 아닙니다.""")
            ])),
            ("enter", AndValidationRule([
                lambda c: (c.name == "enter", "Column 명은 반드시 enter여야 합니다."),
                lambda c: (not c.nullable, "enter는 null이 될 수 없습니다"),
                lambda c: (not c.is_unique, "enter는 Table내에서 고유한 값이 아닙니다."),
                OrValidationRule([
                    # If char / varchar
                    AndValidationRule([
                        lambda c: (c.dtype in ["character", "character varying", "text"], """
                            enter column은 날짜 시간을 표현하기 위해 최소 19자 길이의 char 혹은 varchar가 되어야 합니다.
                            text도 정답으로 처리하지만 19자리 문자를 표현하기 위해 권장되는 타입은 아닙니다.
                        """),
                        lambda c: ((c.dtype == "text" or (c.char_max_len and c.char_max_len >= 19)), """
                            enter column은 날짜 시간을 표현하기 위해 최소 19자 길이의 char 혹은 varchar가 되어야 합니다.
                            text도 정답으로 처리하지만 19자리 문자를 표현하기 위해 권장되는 타입은 아닙니다.
                        """),
                    ]),
                    # If timestamp type
                    lambda c: (c.dtype.startswith("timestamp"), """enter column이 timestamp 혹은 길이가 19 이상인 문자열이어야 합니다.""")
                ])
            ])),
            ("out", AndValidationRule([
                lambda c: (c.name == "out", "Column 명은 반드시 out여야 합니다."),
                lambda c: (c.nullable, "out는 null이 될 수 있습니다"),
                lambda c: (not c.is_unique, "out는 Table내에서 고유한 값이 아닙니다."),
                OrValidationRule([
                    # If char / varchar
                    AndValidationRule([
                        lambda c: (c.dtype in ["character", "character varying", "text"], """
                                        out column은 날짜 시간을 표현하기 위해 최소 19자 길이의 char 혹은 varchar가 되어야 합니다.
                                        text도 정답으로 처리하지만 19자리 문자를 표현하기 위해 권장되는 타입은 아닙니다.
                                    """),
                        lambda c: ((c.dtype == "text" or (c.char_max_len and c.char_max_len >= 19)), """
                                        out column은 날짜 시간을 표현하기 위해 최소 19자 길이의 char 혹은 varchar가 되어야 합니다.
                                        text도 정답으로 처리하지만 19자리 문자를 표현하기 위해 권장되는 타입은 아닙니다.
                                    """),
                    ]),
                    # If timestamp type
                    lambda c: (c.dtype.startswith("timestamp"), """out column이 timestamp 혹은 길이가 19 이상인 문자열이어야 합니다.""")
                ])
            ])),
            ("purpose", AndValidationRule([
                lambda c: (c.name == "purpose", "Column 명은 반드시 purpose여야 합니다."),
                lambda c: (c.nullable, "purpose는 null이 될 수 있습니다"),
                lambda c: (not c.is_unique, "purpose는 Table내에서 고유한 값이 아닙니다"),
                lambda c: ((c.dtype == "text" or (c.char_max_len and c.char_max_len >= 50)), "purpose는 최소 50자 이상을 허용해야 합니다."),
                lambda c: (c.dtype in ["character", "character varying", "text"],
                           """purpose는 char혹은 varchar 타입이어야 합니다. text도 정답으로 처리하지만 
                           50자리 문자를 표현하기 위해 권장되는 타입은 아닙니다.""")
            ]))
        ]


class Q4Score(InsertRecordProblem):
    def __init__(self):
        super().__init__("q4_insert_visit_log_table", 5, "visit_log")

    def order_by_col(self):
        return "coalesce(visitor, ''), enter"

    def get_expected_data(self) -> list:
        return [
            (None, datetime.strptime('2022-07-11 12:30:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-11 14:45:00', '%Y-%m-%d %H:%M:%S'), 'meeting'),
            (None, datetime.strptime('2022-07-12 15:20:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-12 16:50:00', '%Y-%m-%d %H:%M:%S'), 'visit family'),
            ('A00001', datetime.strptime('2022-07-11 11:00:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-11 18:00:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('A00001', datetime.strptime('2022-07-12 08:15:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-12 17:56:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('A00001', datetime.strptime('2022-07-13 09:00:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-13 18:20:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('A00001', datetime.strptime('2022-07-14 08:30:00', '%Y-%m-%d %H:%M:%S'), None, 'work'),
            ('A08771', datetime.strptime('2022-07-11 09:00:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-11 17:56:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('A08771', datetime.strptime('2022-07-12 09:20:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-12 18:20:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('A08771', datetime.strptime('2022-07-13 09:20:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-13 18:00:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('A08771', datetime.strptime('2022-07-14 08:30:00', '%Y-%m-%d %H:%M:%S'), None, 'work'),
            ('B00100', datetime.strptime('2022-07-11 10:00:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-11 19:00:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('B00100', datetime.strptime('2022-07-12 08:30:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-12 19:00:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('B00100', datetime.strptime('2022-07-13 08:30:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-13 18:00:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('B00100', datetime.strptime('2022-07-14 08:30:00', '%Y-%m-%d %H:%M:%S'), None, 'work'),
            ('C00001', datetime.strptime('2022-07-11 09:20:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-11 18:00:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('C00001', datetime.strptime('2022-07-12 10:00:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-12 18:00:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('C00001', datetime.strptime('2022-07-13 09:20:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-13 18:20:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('C00002', datetime.strptime('2022-07-11 09:30:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-11 18:20:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('C00002', datetime.strptime('2022-07-12 09:00:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-12 17:56:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('C00002', datetime.strptime('2022-07-13 08:15:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-13 17:56:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('C00129', datetime.strptime('2022-07-11 09:00:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-11 18:20:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('C00129', datetime.strptime('2022-07-12 10:00:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-12 18:00:00', '%Y-%m-%d %H:%M:%S'), 'work'),
            ('C00129', datetime.strptime('2022-07-13 10:00:00', '%Y-%m-%d %H:%M:%S'),
             datetime.strptime('2022-07-13 18:00:00', '%Y-%m-%d %H:%M:%S'), 'work')
        ]