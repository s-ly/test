import sqlite3 as sql
import time

def tik():
    SQL = f"SELECT my_stroke FROM int_test WHERE id = 1"
    with sql.connect('testDB.db') as connect_db:
        cursor_db = connect_db.cursor()
        cursor_db.execute(SQL)
        SQL_result = cursor_db.fetchall()   
        print(SQL_result[0][0])

while True:
    time.sleep(1)
    tik()