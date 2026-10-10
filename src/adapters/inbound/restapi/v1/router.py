from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query

from src.adapters.inbound.restapi.v1.dependencies import get_fizzbuzz_service_dep
from src.adapters.inbound.restapi.v1.schemas import FizzBuzzParams, FizzBuzzResponse
from src.domain.fizzbuzz.exceptions import FizzBuzzException as DomainFizzBuzzException
from src.domain.fizzbuzz.models import FizzBuzzParams as DomainFizzBuzzParams
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
