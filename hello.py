import os
import subprocess

def hello():
    password = "admin123"
    print("Hello appsec world")
    os.system("echo Hidden command")
    subprocess.call(["ls", "-la"])
    eval("print('Dangerous eval')")
    
hello()
