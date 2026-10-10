from functools import lru_cache
from typing import Annotated

from fastapi import Depends

from src.adapters.outbound.in_memory_stats_store_adapter import (
    InMemoryFizzBuzzStatsStoreAdapter,
)
from src.domain.fizzbuzz.ports import FizzBuzzStatsPort
from src.domain.fizzbuzz.service import FizzBuzzService


@lru_cache(maxsize=1)
def get_stats_store_dep() -> FizzBuzzStatsPort:
    return InMemoryFizzBuzzStatsStoreAdapter()


def get_fizzbuzz_service_dep(
    stats_store: Annotated[FizzBuzzStatsPort, Depends(get_stats_store_dep)],
) -> FizzBuzzService:
    return FizzBuzzService(stats_store=stats_store)
