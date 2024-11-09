import sqlite3
from random import randint as rdi

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER,
username TEXT,
first_name TEXT,
block INTEGER);
""")

def add_user(id_user, username, first_name):
    check_user = cursor.execute(f'SELECT * FROM Users WHERE id={id_user}')

    if check_user.fetchone() is None:
        cursor.execute(f'INSERT INTO Users VALUES("{id_user}", "{username}", "{first_name}", 0)')
    connection.commit()


connection.commit()
connection.close()
