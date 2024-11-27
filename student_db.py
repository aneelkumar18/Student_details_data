import sqlite3

# Connect to SQLite database (it will create the database file if it doesn't exist)
conn = sqlite3.connect('student_db.db')
cursor = conn.cursor()

# Create a table to store student details
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        roll_no TEXT NOT NULL,
        course TEXT NOT NULL
    )
''')

# Commit changes and close connection
conn.commit()
conn.close()
