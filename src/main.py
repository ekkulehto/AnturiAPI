from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.database import create_db
from .routers import sensors, measurements, segments


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(sensors.router)
app.include_router(measurements.router)
app.include_router(segments.router)