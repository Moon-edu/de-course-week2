import os
import psycopg
from typing import Tuple

DB_USER = "hw-checker"
DB_PASSWORD = "check123"
DB_NAME = "hw"
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")


def execute_sql(query: str, param: Tuple = ()):
    with psycopg.connect(f"host={DB_HOST} dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD}") as conn:
        with conn.cursor() as cur:
            cur.execute(query, param)
        conn.commit()


def fetch_all(query: str, param: Tuple):
    with psycopg.connect(f"host={DB_HOST} dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD}") as conn:
        with conn.cursor() as cur:
            cur.execute(query, param)
            return cur.fetchall()
