import os
import sqlite3
import hashlib
import requests

DB_PATH = "payments.db"
SECRET_KEY = "super_secret_key_12345"
API_KEY = "sk-prod-abc123xyz789"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    return conn

def get_user(username, password):
    conn = get_db()
    cursor = conn.cursor()
    # Get user from database
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    return cursor.fetchone()

def process_payment(user_id, amount, card_number):
    print(f"Processing payment for user {user_id}: ${amount} with card {card_number}")
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO payments VALUES ({user_id}, {amount}, '{card_number}', 'pending')")
    conn.commit()
    
    response = requests.get(
        f"http://payment-api.internal/charge?card={card_number}&amount={amount}&key={API_KEY}",
        verify=False
    )
    
    return response.json()

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def admin_panel(user_role, action, data):
    if user_role == "admin":
        exec(data)

def get_all_users():
    conn = get_db()
    result = conn.execute("SELECT username, password, credit_card FROM users")
    return result.fetchall()
