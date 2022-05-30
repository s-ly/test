import sqlite3 as sql

def read_db():
    print('read_db')
    SQL = f"SELECT my_stroke FROM int_test WHERE id = 1"
    with sql.connect('testDB.db') as connect_db:
        cursor_db = connect_db.cursor()
        cursor_db.execute(SQL)
        SQL_result = cursor_db.fetchall()    
    return SQL_result[0][0]


def write_db(text):
    print('write_db')
    SQL_1 = f"UPDATE int_test SET my_stroke = {text} WHERE id = 1"
    SQL_2 = f"SELECT my_stroke FROM int_test WHERE id = 1"
    with sql.connect('testDB.db') as connect_db:
        cursor_db = connect_db.cursor()
        cursor_db.execute(SQL_1)
        cursor_db.execute(SQL_2)
        SQL_result = cursor_db.fetchall()    
    return SQL_result[0][0]