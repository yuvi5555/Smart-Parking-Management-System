import sqlite3

# Connect to your database file
conn = sqlite3.connect("parking.db")
cursor = conn.cursor()

# Drop the old vehicles table if it exists
cursor.execute("DROP TABLE IF EXISTS vehicles")

conn.commit()
conn.close()

print("✅ Old 'vehicles' table dropped successfully.")
