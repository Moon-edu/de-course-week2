import pytest
from score.criteria import Q1Score
import logging
from util import dbutil


@pytest.fixture(autouse=True)
def drop_schema_if_exist():
    logging.info("DROP schema public")
    dbutil.execute_sql(f"drop schema if exists public CASCADE")
    logging.info("Dropped schema, creating schema")
    dbutil.execute_sql(f"create schema if not exists public")


def test_sql(drop_schema_if_exist):
    # sql_files = [
    #     Q1Score("q1_create_employee_table", 10),
    #     ("q2_insert_employee_table", 5),
    #     ("q3_create_visit_log_table", 10),
    #     ("q4_insert_visit_log_table", 5),
    #     ("q5_employee_female", 10),
    #     ("q6_employee_male", 10),
    #     ("q7_visit_log_cnt", 10),
    #     ("q8_visit_log_group_by_purpose_cnt", 10),
    #     ("q9_find_visit_employee", 10),
    #     ("q10_update_peach_position", 10),
    #     ("q11_delete_null_visit", 10)
    # ]

    print(f"""Score {Q1Score("q1_create_employee_table", 10, "employee").score()}""")
    # with open("homework/q1_create_employee_table.sql", "r") as f:
    #     query = f.read()
    #     try:
    #         execute_sql(query, False)
    #     except Exception as e:


