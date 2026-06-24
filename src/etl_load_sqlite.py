import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "data", "raw", "customers_raw.csv")
DB_PATH = os.path.join(BASE_DIR, "data", "db", "analytics.db")


def load_csv_to_sqlite():
    df = pd.read_csv(CSV_PATH)
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        df.to_sql("customers_raw", conn, if_exists="replace", index=False)


if __name__ == "__main__":
    load_csv_to_sqlite()
    print(f"Loaded {CSV_PATH} into {DB_PATH}")
