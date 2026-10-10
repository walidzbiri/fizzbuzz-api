import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.adapters.inbound.restapi.v1 import app_v1

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    logger.info("Starting application...")
    yield
    logger.info("Shutting down application...")


app = FastAPI(title="FizzBuzz API", lifespan=lifespan, root_path="/api")


@app.get("/health-check", tags=["Health"])
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "fizzbuzz-api"}


app.mount("/v1", app_v1)
