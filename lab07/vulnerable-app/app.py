import subprocess
import pickle
import base64
import os
import sqlite3

# Hardcoded credentials
DB_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"
SECRET_TOKEN = "ghp_abc123def456ghi789"

def sql_injection(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Уязвимость: прямая вставка в запрос
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

def command_injection(user_input):
    # Уязвимость: прямой вызов shell
    subprocess.call(f"echo {user_input}", shell=True)

def unsafe_pickle(data):
    # Уязвимость: десериализация pickle
    decoded = base64.b64decode(data)
    return pickle.loads(decoded)

def eval_injection(expression):
    # Уязвимость: eval от пользовательского ввода
    return eval(expression)

# Небезопасная конфигурация
os.environ['SECRET_KEY'] = 'super_secret_key_123'

if __name__ == "__main__":
    print("Vulnerable app started")
