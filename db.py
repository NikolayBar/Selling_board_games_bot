import sqlite3
from random import randint as rdi

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
 username TEXT NOT NULL,
 email TEXT NOT NULL,
 ags INTEGER
 )
 """)

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users(email)")

# cursor.execute("INSERT INTO Users (username, email, ags) VALUES(?, ?, ?)", ("newuser", "ex@mail.ru", "28"))
# for i in range(30):
#     cursor.execute("INSERT INTO Users (username, email, ags) VALUES(?, ?, ?)",
#                    (f"{i}newuser", f"{i}ex@mail.ru", f"{rdi(22, 60)}"))

# cursor.execute("UPDATE Users SET ags=? WHERE username=?", (39, "newuser"))
# cursor.execute("DELETE FROM Users WHERE username=?", ("newuser",))

# cursor.execute("SELECT * FROM Users")
# cursor.execute("SELECT username, ags FROM Users WHERE ags > ?", (29,))
# cursor.execute("SELECT username, ags FROM Users GROUP BY ags")
# cursor.execute("SELECT username, ags FROM Users WHERE (ags > ? AND ags < ?)", (40, 50))
a, b = 45, 50
cursor.execute(f"SELECT username, ags FROM Users WHERE (ags > {a} AND ags < {b}) ORDER BY ags")

users = cursor.fetchall()
for user in users:
    print(*user, sep=': ')


connection.commit()
connection.close()
