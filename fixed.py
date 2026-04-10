import sqlite3
import os
import secrets

# Fix 1: Use environment variable instead of hardcoded password
DB_PASSWORD = os.environ.get('DB_PASSWORD')

def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Fix 2: Parameterized query to prevent SQL injection
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchall()

def generate_token():
    # Fix 3: Secure random token
    return str(secrets.randbelow(900000) + 100000)

# Fix 4: Removed unused variable

print(get_user('admin'))
print(generate_token())
