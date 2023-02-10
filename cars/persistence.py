from cars.database import get_connection


def get_all_cars():
    cursor = get_connection().cursor()
    cursor.execute("SELECT * FROM cars")
    return cursor.fetchall()
