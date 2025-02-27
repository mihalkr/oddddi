import sqlite3

connection = sqlite3.connect("db1.sl3", 5)
cur = connection.cursor()

# cur.execute("CREATE TABLE Students (name TEXT, age INTEGER, groupname)")
# connection.commit()

name= input("name: ")
age = input("age: ")
group= input("group: ")
cur.execute(f"INSERT INTO Students (name, age, groupname) VALUES ('{name}','{age}','{group}');")
connection.commit()

connection.close()