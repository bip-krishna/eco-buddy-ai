import sqlite3

DB_NAME = "eco_buddy.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assessments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            transport TEXT,
            distance REAL,
            electricity REAL,
            diet TEXT,
            flights INTEGER,
            footprint REAL,
            eco_score INTEGER
        )
    """)

    conn.commit()
    conn.close()


def save_assessment(
    transport,
    distance,
    electricity,
    diet,
    flights,
    footprint,
    eco_score
):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO assessments (
            transport,
            distance,
            electricity,
            diet,
            flights,
            footprint,
            eco_score
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        transport,
        distance,
        electricity,
        diet,
        flights,
        footprint,
        eco_score
    ))

    conn.commit()
    conn.close()


def get_assessments():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM assessments
        ORDER BY date DESC
    """)

    data = cursor.fetchall()

    conn.close()
    return data