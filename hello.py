import os
import subprocess

name = input("Enter your name: ")
password = "admin123"
print(f"Hello appsec world from @{name}")
os.system("echo Hidden command")
subprocess.call(["ls", "-la"])
eval("print('Dangerous eval')")
