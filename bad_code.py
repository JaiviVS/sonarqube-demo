# bad_code.py - Full of issues for SonarQube to detect

import os
import sys

password = "admin123"  # Hardcoded credential (Security issue)
API_KEY = "12345-abcde-secret-key"  # Another secret

def divide(a,b):  # Missing spaces (style issue)
    result = a/b  # No zero-division check (Bug)
    return result

def unused_function():  # Dead code
    pass

def process_user_input(user_input):
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"  # SQL Injection!
    return query

class myClass:  # Naming convention issue (should be MyClass)
    def __init__(self):
        self.data = []
    
    def add_data(self, item):
        self.data.append(item)
        self.data.append(item)  # Duplicate line
    
    def get_data(self):
        return self.data

x = 10
y = 20
z = x+y  # Unused variable, no spaces

def login(username, password):
    if username == "admin" and password == "admin123":  # Hardcoded creds again
        return True

def read_file(filename):
    f = open(filename, 'r')  # File never closed (resource leak)
    data = f.read()
    return data

def calculate(nums):
    total = 0
    for i in range(len(nums)):  # Should use enumerate or direct iteration
        total = total + nums[i]
    return total

try:
    result = divide(10, 0)
except Exception as e:
    pass
