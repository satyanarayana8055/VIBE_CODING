import os
import sqlite3
import pandas as pd
import pytest

from src.kpi_city import city_kpi

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "db", "analytics.db")
CSV_PATH = os.path.join(BASE_DIR, "data", "raw", "customers_raw.csv")


def setup_module(module):
    df = pd.read_csv(CSV_PATH)
    with sqlite3.connect(DB_PATH) as conn:
        df.to_sql("customers_raw", conn, if_exists="replace", index=False)


def test_city_kpi_happy_path():
    rows = city_kpi("Mumbai")
    assert all(row[1] == "Mumbai" for row in rows)
    assert len(rows) == 3


def test_city_kpi_injection_attempt():
    rows = city_kpi("Mumbai' OR 1=1 --")
    assert rows == []
