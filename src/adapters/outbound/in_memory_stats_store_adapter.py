import threading

from src.domain.fizzbuzz.models import FizzBuzzParams, FizzBuzzStatsEntry
from src.domain.fizzbuzz.ports import FizzBuzzStatsPort


class InMemoryFizzBuzzStatsStoreAdapter(FizzBuzzStatsPort):
    def __init__(self) -> None:
        self._stats: dict[str, FizzBuzzStatsEntry] = {}
        self._lock = threading.Lock()

    def _key(self, params: FizzBuzzParams) -> str:
        return f"{params.int1}:{params.int2}:{params.limit}:{params.str1}:{params.str2}"

    def record(self, params: FizzBuzzParams) -> None:
        key = self._key(params)
        with self._lock:
            old_entry = self._stats.get(key)
            hits = old_entry.hits + 1 if old_entry else 1
            self._stats[key] = FizzBuzzStatsEntry(params=params, hits=hits)

    def get_most_frequent(self) -> FizzBuzzStatsEntry | None:
        with self._lock:
            snapshot = list(self._stats.values())
        if not snapshot:
            return None
        return max(snapshot, key=lambda x: x.hits)
