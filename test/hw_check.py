import pytest
from score.criteria import *
import logging
from util import dbutil
import base64
from data.all_data import ALL_EMPLOYEE, ALL_VISIT_LOG


def drop_schema_if_exist():
    logging.info("DROP schema public")
    dbutil.execute_sql(f"drop schema if exists public CASCADE")
    logging.info("Dropped schema, creating schema")
    dbutil.execute_sql(f"create schema if not exists public")

def create_tables():
    dbutil.execute_sql(base64.b64decode("Y3JlYXRlIHRhYmxlIGVtcGxveWVlKAoJZW1wX2lkIHZhcmNoYXIoMTApIHVuaXF1ZSBub3Qgbn"
    + "VsbCwKCWdlbmRlciB2YXJjaGFyKDEwKSBub3QgbnVsbCwKCW5hbWUgdmFyY2hhcigyMCkgbm90IG51bGwsCglhZGRyZXNzIHZhcmNoYXIoMTAwK"
    + "SBudWxsLAoJZGVwYXJ0bWVudCBzbWFsbGludCBudWxsLAoJbWFuYWdlciB2YXJjaGFyKDEwMCkgbnVsbCwKCWFnZSBpbnQgbm90IG51bGwsCglwb"
    + "3NpdGlvbiB2YXJjaGFyKDIwMCkgbnVsbAop"))

    dbutil.execute_sql(base64.b64decode("Y3JlYXRlIHRhYmxlIHZpc2l0X2xvZygKCXZpc2l0b3IgdmFyY2hhcig2KSBudWxsLAoJZW50ZXIgd"
    + "GltZXN0YW1wIG5vdCBudWxsLAoJb3V0IHRpbWVzdGFtcCwKCXB1cnBvc2UgdmFyY2hhcig1MCkKKQ=="))

def insert_data():
    for e in ALL_EMPLOYEE:
        dbutil.execute_sql(base64.b64decode("SU5TRVJUIElOVE8gZW1wbG95ZWUgdmFsdWVzKCVzLCAlcywgJXMsICVzLCAlcywgJXMsICVz"
                                        + "LCAlcyk="), e)
    for v in ALL_VISIT_LOG:
        dbutil.execute_sql(base64.b64decode("SU5TRVJUIElOVE8gdmlzaXRfbG9nIHZhbHVlcyglcywgJXMsICVzLCAlcyk="), v)


def test_sql():
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

    drop_schema_if_exist()
    create_tables()
    insert_data()
    my_score = Q11Score().score()

    print(f"""Score {my_score}""")
    # with open("homework/q1_create_employee_table.sql", "r") as f:
    #     query = f.read()
    #     try:
    #         execute_sql(query, False)
    #     except Exception as e:


