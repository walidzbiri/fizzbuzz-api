from fastapi import FastAPI

from src.adapters.inbound.restapi.v1.router import router

app_v1 = FastAPI(
    title="FizzBuzz API",
    description="An API that returns the FizzBuzz sequence for a given range of numbers.",
    version="1.0",
)

app_v1.include_router(router)
