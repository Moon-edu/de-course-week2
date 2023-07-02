import os
import psycopg
from typing import Tuple

DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_NAME = "postgres"
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")


def execute_sql(query: str, param: Tuple = ()):
    with psycopg.connect(f"host={DB_HOST} dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD}") as conn:
        with conn.cursor() as cur:
            cur.execute(query, param)
        conn.commit()


def fetch_all(query: str, param: Tuple = ()) -> list:
    with psycopg.connect(f"host={DB_HOST} dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD}") as conn:
        with conn.cursor() as cur:
            cur.execute(query, param)
            return cur.fetchall()


def check_table_exists(table_name):
    query = f"select exists(select * from information_schema.tables where table_name=%s)"
    return fetch_all(query, (table_name, ))[0][0]