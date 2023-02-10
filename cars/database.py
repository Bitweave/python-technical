import sqlite3


def get_connection():
    connection = sqlite3.connect("cars.db")
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    cursor = get_connection().cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS cars(id INTEGER PRIMARY KEY AUTOINCREMENT, model, make, colour, age)")
    cursor.close()
