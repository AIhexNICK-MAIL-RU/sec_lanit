import subprocess
import pickle
import base64
import os
import sqlite3
from getpass import getpass

# Исправление: секреты из переменных окружения
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
API_KEY = os.environ.get('API_KEY', '')
SECRET_TOKEN = os.environ.get('SECRET_TOKEN', '')

def sql_injection(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Исправление: параметризованный запрос
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchall()

def command_injection(user_input):
    # Исправление: без shell=True
    subprocess.call(["echo", user_input])

def unsafe_pickle(data):
    # Исправление: использование json вместо pickle
    import json
    decoded = base64.b64decode(data)
    return json.loads(decoded)

def eval_injection(expression):
    # Исправление: валидация ввода
    allowed = set("0123456789+-*/() ")
    if all(c in allowed for c in expression):
        return eval(expression)
    return "Invalid expression"

# Безопасная конфигурация
os.environ['SECRET_KEY'] = os.environ.get('SECRET_KEY', '')

if __name__ == "__main__":
    print("Secure app started")
