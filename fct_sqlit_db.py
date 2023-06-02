import sqlite3

connectionString =sqlite3.connect('fct_db')
cursor = connectionString.cursor()

cursor.execute('''CREATE TABLE demo (id INTEGER, demo_name TEXT, demo_password TEXT)''')
