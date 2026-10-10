from src.domain.fizzbuzz.models import FizzBuzzParams
from src.domain.fizzbuzz.ports import FizzBuzzStatsPort


class FizzBuzzService:
    def __init__(self, stats_store: FizzBuzzStatsPort) -> None:
        self._stats_store = stats_store

    def generate(self, params: FizzBuzzParams) -> list[str]:
        self._stats_store.record(params)

        result: list[str] = []
        for n in range(1, params.limit + 1):
            is_multiple_of_int1 = n % params.int1 == 0
            is_multiple_of_int2 = n % params.int2 == 0

            if is_multiple_of_int1 and is_multiple_of_int2:
                result.append(params.str1 + params.str2)
            elif is_multiple_of_int1:
                result.append(params.str1)
            elif is_multiple_of_int2:
                result.append(params.str2)
            else:
                result.append(str(n))

        return result
