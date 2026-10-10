from src.domain.fizzbuzz.models import FizzBuzzParams, FizzBuzzStatsEntry
from src.domain.fizzbuzz.ports import FizzBuzzStatsPort


class InMemoryFizzBuzzStatsStoreAdapter(FizzBuzzStatsPort):
    def __init__(self) -> None:
        self._stats: dict[str, FizzBuzzStatsEntry] = {}

    def _key(self, params: FizzBuzzParams) -> str:
        return f"{params.int1}:{params.int2}:{params.limit}:{params.str1}:{params.str2}"

    def record(self, params: FizzBuzzParams) -> None:
        key = self._key(params)
        if key in self._stats:
            old_entry = self._stats[key]
            self._stats[key] = FizzBuzzStatsEntry(
                params=old_entry.params,
                hits=old_entry.hits + 1,
            )
        else:
            self._stats[key] = FizzBuzzStatsEntry(params)

    def get_most_frequent(self) -> FizzBuzzStatsEntry | None:
        if not self._stats:
            return None
        return max(self._stats.values(), key=lambda x: x.hits)
