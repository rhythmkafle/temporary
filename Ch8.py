'''
Ch8 - Advanced Topics

Working with Database and SQL statements    
    - we will use SQLite3 for simplicity
'''
# Importing and connecting
import sqlite3
conn = sqlite3.connect('example.db')

# Creating a cursor and a table
c = conn.cursor()
c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

'''
A cursor is an object used to interact with a database. It allows you to execute SQL queries and fetch results.
'''

# Inserting Records
c.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25)) # Alice is set in the first ?,  25 in the second ?. This is called prepare and bind and helps in secure coding

# Fetching Records
c.execute("SELECT * FROM users")
print(c.fetchall())

# committing and closing
conn.commit()
conn.close()


# Proper example: to perform CRUD operations and print employees with salary > 25000: ( 10 marks )
import sqlite3

# Connect to database (or create it)
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    salary REAL
)
''')

# ------------------- CRUD OPERATIONS -------------------

# Create (Insert)
cursor.execute("INSERT INTO employees (name, age, salary) VALUES (?, ?, ?)", ("Alice", 30, 30000))
cursor.execute("INSERT INTO employees (name, age, salary) VALUES (?, ?, ?)", ("Bob", 25, 22000))
cursor.execute("INSERT INTO employees (name, age, salary) VALUES (?, ?, ?)", ("Charlie", 35, 27000))

# Read (Select)
print("\nEmployees with salary > 25000:")
cursor.execute("SELECT * FROM employees WHERE salary > 25000")
for row in cursor.fetchall():
    print(row)

# Update
cursor.execute("UPDATE employees SET salary = 28000 WHERE name = 'Bob'")

# Delete
cursor.execute("DELETE FROM employees WHERE name = 'Charlie' AND salary < 26000")

# Commit changes and close
conn.commit()
conn.close()
