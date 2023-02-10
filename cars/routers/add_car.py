from fastapi import APIRouter

from cars import persistence

add_car_router = APIRouter()


@add_car_router.post("/cars")
def add_car(model: str, make: str, colour: str, age: int):
    return persistence.add_car(model, make, colour, age)
