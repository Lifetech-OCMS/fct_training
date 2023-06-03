import sqlite3

connectionString =sqlite3.connect('fct_db')
mycursor = connectionString.cursor()

mycursor.execute('CREATE TABLE IF NOT EXISTS demo (id INTEGER, demo_name TEXT, demo_password TEXT)') 
mycursor.execute("INSERT INTO demo (demo_name, demo_password) VALUES('Akinde','Fct12345')")
mycursor.execute("INSERT INTO demo (demo_name, demo_password) VALUES('Ayobami','Fct892')")
mycursor.execute("INSERT INTO demo (demo_name, demo_password) VALUES('Ajayi','Fct921')")
connectionString.commit()
mycursor.execute("SELECT * FROM demo")
print(mycursor.fetchall())
