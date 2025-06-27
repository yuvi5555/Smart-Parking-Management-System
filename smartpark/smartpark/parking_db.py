import sqlite3
from datetime import datetime

def create_tables():
    conn = sqlite3.connect("parking.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehicles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            plate TEXT,
            slot TEXT,
            entry_time TEXT,
            exit_time TEXT,
            duration TEXT
        )
    """)

    conn.commit()
    conn.close()

def add_vehicle(username, plate, slot):
    entry_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect("parking.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO vehicles (username, plate, slot, entry_time, exit_time, duration)
        VALUES (?, ?, ?, ?, NULL, NULL)
    """, (username, plate, slot, entry_time))

    conn.commit()
    conn.close()

def get_all_vehicles():
    conn = sqlite3.connect("parking.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vehicles WHERE exit_time IS NULL")
    data = cursor.fetchall()
    rows = []
    for row in data:
        entry_time = datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S")
        now = datetime.now()
        duration = str(now - entry_time).split('.')[0]
        rows.append((*row[:6], duration))
    conn.close()
    return rows

def remove_vehicle_by_slot(slot):
    conn = sqlite3.connect("parking.db")
    cursor = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        UPDATE vehicles SET exit_time = ?, duration = (
            CAST((JULIANDAY(?) - JULIANDAY(entry_time)) * 24 * 60 AS INTEGER) || ' mins'
        ) WHERE slot = ? AND exit_time IS NULL
    """, (now, now, slot))
    conn.commit()
    conn.close()
