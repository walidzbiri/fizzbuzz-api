from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query

from src.adapters.inbound.restapi.v1.dependencies import (
    get_fizzbuzz_service_dep,
    get_stats_store_dep,
)
from src.adapters.inbound.restapi.v1.schemas import (
    FizzBuzzParams,
    FizzBuzzResponse,
    FizzBuzzStatsResponse,
)
from src.domain.fizzbuzz.exceptions import FizzBuzzException as DomainFizzBuzzException
from src.domain.fizzbuzz.models import FizzBuzzParams as DomainFizzBuzzParams
from src.domain.fizzbuzz.ports import FizzBuzzStatsPort
from src.domain.fizzbuzz.service import FizzBuzzService

router = APIRouter()


@router.get("/fizzbuzz", response_model=FizzBuzzResponse)
def get_fizzbuzz_sequence(
    fizzbuzz_service: Annotated[FizzBuzzService, Depends(get_fizzbuzz_service_dep)],
    params: Annotated[FizzBuzzParams, Query()],
) -> FizzBuzzResponse:
    try:
        domain_params = DomainFizzBuzzParams(
            int1=params.int1,
            int2=params.int2,
            limit=params.limit,
            str1=params.str1,
            str2=params.str2,
        )
    except DomainFizzBuzzException as e:
        raise HTTPException(status_code=400, detail=str(e))

    result = fizzbuzz_service.generate(domain_params)
    return FizzBuzzResponse(result)


@router.get("/stats", response_model=FizzBuzzStatsResponse)
def get_stats(
    stats_store: Annotated[FizzBuzzStatsPort, Depends(get_stats_store_dep)],
) -> FizzBuzzStatsResponse:
    most_frequent = stats_store.get_most_frequent()
    if most_frequent is None:
        raise HTTPException(status_code=404, detail="No requests recorded yet")
    return FizzBuzzStatsResponse(
        int1=most_frequent.params.int1,
        int2=most_frequent.params.int2,
        limit=most_frequent.params.limit,
        str1=most_frequent.params.str1,
        str2=most_frequent.params.str2,
        hits=most_frequent.hits,
    )
