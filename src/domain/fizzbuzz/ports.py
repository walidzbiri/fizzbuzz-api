from abc import ABC, abstractmethod

from src.domain.fizzbuzz.models import FizzBuzzParams, FizzBuzzStatsEntry


class FizzBuzzStatsPort(ABC):
    @abstractmethod
    def record(self, params: FizzBuzzParams) -> None:
        pass

    @abstractmethod
    def get_most_frequent(self) -> FizzBuzzStatsEntry | None:
        pass
