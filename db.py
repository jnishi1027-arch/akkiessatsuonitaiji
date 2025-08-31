import sqlite3

DATABASE = 'database.db'

def create_productions_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS productions (arrival_day, title, price)")
    con.close()
