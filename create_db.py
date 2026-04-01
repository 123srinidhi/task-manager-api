import sqlite3

conn = sqlite3.connect("tasks.db")

conn.execute("""
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    status TEXT NOT NULL
)
""")

conn.close()

print("Database created successfully!")
