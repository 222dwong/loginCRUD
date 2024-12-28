import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE users (username TEXT, password TEXT)''')

# Insert sample data
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("testuser", "password123"))
conn.commit()
conn.close()