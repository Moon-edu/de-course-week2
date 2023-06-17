import logging
import pytest
import base64
from tests.score.criteria import *
from util.dbutil import *


def execute_sql_file(filename):
    with open(f"homework/{filename}.sql", "r") as f:
        query = f.read()
        try:
            logging.info(f"Executing: {query}")
            execute_sql(query)
        except Exception as e:
            logging.error(e)
            raise e


def _create_employee_table():
    execute_sql_file("q1_create_employee_table")

def _create_visit_log_table():
    execute_sql_file("q3_create_visit_log_table")

@pytest.fixture
def drop_schema_if_exist():
    logging.info("DROP schema public")
    execute_sql(f"drop schema if exists public CASCADE")


@pytest.fixture
def create_schema_if_not_exist():
    logging.info("Create schema")
    execute_sql(f"create schema if not exists public")


@pytest.fixture
def create_employee_table():
    logging.info("Create employee table")
    _create_employee_table()

@pytest.fixture
def create_visit_log_table():
    logging.info("Create visit_log table")
    _create_visit_log_table()

@pytest.fixture
def prepare_employees():
    for e in ALL_EMPLOYEE:
        execute_sql(base64.b64decode("SU5TRVJUIElOVE8gZW1wbG95ZWUgdmFsdWVzKCVzLCAlcywgJXMsICVzLCAlcywgJXMsICVz"
                                        + "LCAlcyk="), e)

@pytest.fixture
def prepare_visit_logs():
    for v in ALL_VISIT_LOG:
        execute_sql(base64.b64decode("SU5TRVJUIElOVE8gdmlzaXRfbG9nIHZhbHVlcyglcywgJXMsICVzLCAlcyk="), v)


def test_create_employee_table(drop_schema_if_exist, create_schema_if_not_exist):
    _create_employee_table()

    score = Q1Score().score()
    logging.info(f"Q1 Score: {score}")


def test_create_employees(drop_schema_if_exist, create_schema_if_not_exist, create_employee_table):
    execute_sql_file("q2_insert_employee_table")

    score = Q2Score().score()
    logging.info(f"Q2 Score: {score}")


def test_create_visit_log_table(drop_schema_if_exist, create_schema_if_not_exist):
    _create_visit_log_table()

    score = Q3Score().score()
    logging.info(f"Q3 Score: {score}")


def test_create_visit_logs(drop_schema_if_exist, create_schema_if_not_exist, create_visit_log_table):
    execute_sql_file("q4_insert_visit_log_table")

    score = Q4Score().score()
    logging.info(f"Q4 Score: {score}")


def test_female_employee(drop_schema_if_exist, create_schema_if_not_exist, create_employee_table, prepare_employees):
    execute_sql_file("q5_employee_female")

    score = Q5Score().score()
    logging.info(f"Q5 Score: {score}")


def test_male_employee(drop_schema_if_exist, create_schema_if_not_exist, create_employee_table, prepare_employees):
    execute_sql_file("q6_employee_male")

    score = Q6Score().score()
    logging.info(f"Q6 Score: {score}")


def test_cnt_visit_log(drop_schema_if_exist, create_schema_if_not_exist, create_visit_log_table, prepare_visit_logs):
    execute_sql_file("q7_visit_log_cnt")

    score = Q7Score().score()
    logging.info(f"Q7 Score: {score}")


def test_group_by_visit_log_purpose(drop_schema_if_exist, create_schema_if_not_exist, create_visit_log_table,
                                    prepare_visit_logs):
    execute_sql_file("q8_visit_log_group_by_purpose_cnt")

    score = Q8Score().score()
    logging.info(f"Q8 Score: {score}")


def test_find_visit_employee(drop_schema_if_exist, create_schema_if_not_exist, create_employee_table,
                             prepare_employees, create_visit_log_table, prepare_visit_logs):
    execute_sql_file("q9_find_visit_employee")

    score = Q9Score().score()
    logging.info(f"Q9 Score: {score}")


def test_update_peach_position(drop_schema_if_exist, create_schema_if_not_exist, create_employee_table,
                               prepare_employees):
    execute_sql_file("q10_update_peach_position")

    score = Q10Score().score()
    logging.info(f"Q10 Score: {score}")


def test_delete_null_visit(drop_schema_if_exist, create_schema_if_not_exist, create_visit_log_table,
                           prepare_visit_logs):
    execute_sql_file("q11_delete_null_visit")

    score = Q11Score().score()
    logging.info(f"Q11 Score: {score}")
