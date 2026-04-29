from flask import Flask, request, render_template_string, redirect, make_response, send_from_directory
import sqlite3
import os
import html
from markupsafe import escape

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, role TEXT)''')
    c.execute("DELETE FROM users")
    c.execute("INSERT INTO users VALUES ('admin', 'admin123', 'admin')")
    c.execute("INSERT INTO users VALUES ('user', 'userpass', 'user')")
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template_string('''
    <h1>Vulnerable DAST Demo App</h1>
    <p>Пример уязвимого приложения для лабораторной по DAST.</p>
    <ul>
      <li><a href="/echo?msg=Hello">Reflected XSS / echo</a></li>
      <li><a href="/search?username=admin">SQL Injection / search</a></li>
      <li><a href="/login">Небезопасный логин</a></li>
      <li><a href="/profile">Профиль (зависит от cookie)</a></li>
      <li><a href="/admin">«Админка» без нормальной авторизации</a></li>
      <li><a href="/files/">Directory listing</a></li>
    </ul>
    ''')

# Исправление XSS: экранирование
@app.route('/echo')
def echo():
    msg = request.args.get('msg', '')
    safe_msg = html.escape(msg)
    return render_template_string(f'<h1>Echo</h1><p>Your message: {safe_msg}</p><a href="/">Back</a>')

# Исправление SQL Injection: параметризованные запросы
@app.route('/search')
def search():
    username = request.args.get('username', '')
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    c.execute(query, (username,))
    results = c.fetchall()
    conn.close()
    return render_template_string(f'''
    <h1>Search Results</h1>
    <p>Results: {results}</p>
    <a href="/">Back</a>
    ''')

# Исправление: проверка пароля в БД
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        c.execute(query, (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            resp = make_response(redirect('/profile'))
            resp.set_cookie('username', username, httponly=True)
            resp.set_cookie('role', user[2], httponly=True)
            return resp
        return "Login failed", 401
    return render_template_string('''
    <h1>Login</h1>
    <form method="POST">
      <input type="text" name="username" placeholder="Username"><br>
      <input type="password" name="password" placeholder="Password"><br>
      <input type="submit" value="Login">
    </form>
    <a href="/">Back</a>
    ''')

@app.route('/profile')
def profile():
    username = request.cookies.get('username')
    role = request.cookies.get('role')
    return render_template_string(f'''
    <h1>Profile</h1>
    <p>Username: {html.escape(username) if username else 'None'}</p>
    <p>Role: {html.escape(role) if role else 'None'}</p>
    <a href="/">Back</a>
    ''')

@app.route('/admin')
def admin():
    role = request.cookies.get('role')
    if role == 'admin':
        return render_template_string('<h1>Admin Panel</h1><p>Welcome admin!</p><a href="/">Back</a>')
    return "Access denied", 403

@app.route('/files/')
@app.route('/files/<path:filename>')
def list_files(filename=None):
    if filename:
        if '..' in filename or filename.startswith('/'):
            return "Invalid filename", 400
        return send_from_directory('files', filename)
    files = os.listdir('files')
    return render_template_string(f'''
    <h1>Files</h1>
    <ul>
        {''.join(f'<li><a href="/files/{html.escape(f)}">{html.escape(f)}</a></li>' for f in files)}
    </ul>
    <a href="/">Back</a>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
