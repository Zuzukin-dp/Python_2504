import sqlite3

con = sqlite3.connect("./users.db")
cur = con.cursor()
sql = """
CREATE TABLE IF NOT EXISTS users
(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
first_name VARCHAR(50),
age INTEGER);
"""

cur.execute(sql)

sql_2 = """
CREATE TABLE IF NOT EXISTS phones
(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
phone_number VARCHAR(20),
used_id INTEGER);
"""

cur.execute(sql_2)

con.close()
