import sqlite3
import os

# Dynamically find the absolute path of the project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_NAME = os.path.join(BASE_DIR, "cybertoolkit.db")

try:
    # Connect to the correct database location
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM activity_logs")
    rows = cursor.fetchall()

    print("\n--- 🛡️ CYBERTOOLKIT ACTIVITY LOGS ---")
    if not rows:
        print("No logs found yet.")
    for row in rows:
        print(row)
    print("------------------------------------\n")

    conn.close()

except sqlite3.OperationalError as e:
    print(f"Database Error: Could not read logs. Details: {e}")
    print(f"Expected DB Location: {DB_NAME}")