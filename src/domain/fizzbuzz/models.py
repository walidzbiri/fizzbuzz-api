from dataclasses import dataclass, field

from src.domain.fizzbuzz.exceptions import (
    EmptyStringException,
    InvalidLimitException,
    ZeroDivisorException,
)


@dataclass(frozen=True)
class FizzBuzzParams:
    int1: int
    int2: int
    limit: int
    str1: str
    str2: str

    def __post_init__(self) -> None:
        if self.int1 == 0:
            raise ZeroDivisorException("int1 cannot be zero")
        if self.int2 == 0:
            raise ZeroDivisorException("int2 cannot be zero")
        if self.limit <= 0:
            raise InvalidLimitException("limit must be positive")
        if not self.str1:
            raise EmptyStringException("str1 cannot be empty")
        if not self.str2:
            raise EmptyStringException("str2 cannot be empty")


@dataclass(frozen=True)
class FizzBuzzStatsEntry:
    params: FizzBuzzParams
    hits: int = field(default=1)