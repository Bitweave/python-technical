import logging

import uvicorn
from fastapi import FastAPI

from cars.config import settings
from cars.routers.get_all_cars import get_all_cars_router
from cars.routers.add_car import add_car_router
from cars.database import init_db

logging.basicConfig(level=settings.LOGGING_LEVEL, format="%(levelname)s: %(name)s %(asctime)s:%(message)s")
logger = logging.getLogger("jam_density_bandit.main")

app = FastAPI(title="Cars")
app.include_router(get_all_cars_router)
app.include_router(add_car_router)


@app.on_event("startup")
def on_startup():
    init_db()


if __name__ == "__main__":
    logger.warning("Running from main.py, this entrypoint is for debugging.")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
