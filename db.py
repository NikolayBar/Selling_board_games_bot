import sqlite3

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
#     cursor.execute("INSERT INTO Users (username, email, ags) VALUES(?, ?, ?)", (f"{i}newuser", f"{i}ex@mail.ru", "28"))

# cursor.execute("UPDATE Users SET ags=? WHERE username=?", (39, "newuser"))
# cursor.execute("DELETE FROM Users WHERE username=?", ("newuser",))

connection.commit()
connection.close()
