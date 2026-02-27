import sqlite3
import pandas as pd

# 1. Create a connection to a new database file
conn = sqlite3.connect('company_data.db')
cursor = conn.cursor()

# 2. Create a fake "Employees" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        salary INTEGER
    )
''')

# 3. Insert some fake data
fake_data = [
    (1, 'Alice', 'Sales', 75000),
    (2, 'Bob', 'Engineering', 90000),
    (3, 'Charlie', 'Sales', 65000),
    (4, 'Diana', 'Marketing', 80000),
    (5, 'Evan', 'Engineering', 95000)
]
cursor.executemany('INSERT OR IGNORE INTO employees VALUES (?, ?, ?, ?)', fake_data)

# Save and close
conn.commit()
conn.close()

print("✅ Fake company database ('company_data.db') created successfully!")