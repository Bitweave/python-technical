
from fastapi import APIRouter

from cars import persistence

get_all_cars_router = APIRouter()


@get_all_cars_router.get("/cars")
def get_all_cars():
    return persistence.get_all_cars()
