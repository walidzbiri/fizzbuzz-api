from src.domain.fizzbuzz.service import FizzBuzzService


def get_fizzbuzz_service_dep() -> FizzBuzzService:
    return FizzBuzzService()
