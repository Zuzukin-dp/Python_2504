import sqlite3

con = sqlite3.connect("./users.db")
cur = con.cursor()
create_tbl_users = """
CREATE TABLE IF NOT EXISTS users
(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
first_name VARCHAR(50),
age INTEGER);
"""

cur.execute(create_tbl_users)

create_tbl_phones = """
CREATE TABLE IF NOT EXISTS phones
(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
phone_number VARCHAR(20),
user_id INTEGER);
"""

cur.execute(create_tbl_phones)

con.close()
