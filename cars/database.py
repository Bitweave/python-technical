import sqlite3


def get_connection():
    return sqlite3.connect("cars.db")


def init_db():
    cursor = get_connection().cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS cars(id INTEGER PRIMARY KEY AUTOINCREMENT, model, make, colour, age)")
    cursor.close()
