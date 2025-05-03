
import sqlite3

connect = sqlite3.connect("user.db")
cursor = connect.cursor()

cursor.execute(""" 
                CREATE TABLE IF NOT EXISTS user(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER ,
                email TEXT UNIQUE)""")
    

def register():
    name = input("Видите Ф И О !")
    age = int(input("Видите свой возрастc !"))
    email = input("Видите свой email !")

    cursor.execute(""" INSERT INTO user
                   (name, age, email)
                   VALUES(?,?,?)""",(name , age , email))
    connect.commit()
register()

