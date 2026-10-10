from src.adapters.outbound.in_memory_stats_store_adapter import (
    InMemoryFizzBuzzStatsStoreAdapter,
)
from src.domain.fizzbuzz.models import FizzBuzzParams


class TestInMemoryFizzBuzzStatsStoreAdapter:
    def test_record_new_params(self) -> None:
        store = InMemoryFizzBuzzStatsStoreAdapter()
        params = FizzBuzzParams(int1=3, int2=5, limit=15, str1="Fizz", str2="Buzz")
        store.record(params)
        assert store.get_most_frequent() is not None
        assert store.get_most_frequent().hits == 1

    def test_record_same_params_increments(self) -> None:
        store = InMemoryFizzBuzzStatsStoreAdapter()
        params = FizzBuzzParams(int1=3, int2=5, limit=15, str1="Fizz", str2="Buzz")
        store.record(params)
        store.record(params)
        store.record(params)
        most_frequent = store.get_most_frequent()
        assert most_frequent is not None
        assert most_frequent.hits == 3

    def test_get_most_frequent(self) -> None:
        store = InMemoryFizzBuzzStatsStoreAdapter()
        params1 = FizzBuzzParams(int1=3, int2=5, limit=15, str1="Fizz", str2="Buzz")
        params2 = FizzBuzzParams(int1=2, int2=3, limit=10, str1="A", str2="B")
        store.record(params1)
        store.record(params1)
        store.record(params1)
        store.record(params2)
        most_frequent = store.get_most_frequent()
        assert most_frequent is not None
        assert most_frequent.params == params1
        assert most_frequent.hits == 3

    def test_get_most_frequent_empty_store(self) -> None:
        store = InMemoryFizzBuzzStatsStoreAdapter()
        assert store.get_most_frequent() is None
