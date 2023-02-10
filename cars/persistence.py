from cars.database import get_connection


def get_all_cars():
    cursor = get_connection().cursor()
    cursor.execute("SELECT * FROM cars")
    return cursor.fetchall()


def add_car(model, make, colour, age):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(f"""INSERT INTO cars(model, make, colour, age) VALUES('{model}', '{make}', '{colour}', {age})""")
    connection.commit()
