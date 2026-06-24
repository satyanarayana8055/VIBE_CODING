import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "db", "analytics.db")


def city_kpi(city: str):
    query = "SELECT customer_id, city, monthly_spend, churned FROM customers_raw WHERE city = ?"
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute(query, (city,))
        rows = cursor.fetchall()
    print(f"KPI results for city={city!r}: {rows}")
    return rows


if __name__ == "__main__":
    city_kpi("Mumbai")
    city_kpi("Mumbai' OR 1=1 --")
