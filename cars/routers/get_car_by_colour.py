from fastapi import APIRouter

from cars import persistence

get_car_by_colour_router = APIRouter()


@get_car_by_colour_router.get("/carbycolour")
def get_car_by_colour(colour: str):
    return persistence.get_car_by_colour(colour)
