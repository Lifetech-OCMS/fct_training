
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database ="fct_traning"
)
print("<br>conneting")
print(mydb)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS TodeletePYTHON")
mycursor.execute("SELECT * FROM agents")
print (mycursor.fetchall())
#for x in mycursor:
#  print(x)  
t=4
print(t)
print("<br><B> hello python</B>")
