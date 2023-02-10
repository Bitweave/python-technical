from cars.database import get_connection


def get_all_cars():
    cursor = get_connection().cursor()
    cursor.execute("SELECT * FROM cars")
    return cursor.fetchall()


def get_car_by_colour(colour):
    matching_cars = []
    for car in get_all_cars():
        if car["colour"] == colour:
            matching_cars.append(car)
    return matching_cars
