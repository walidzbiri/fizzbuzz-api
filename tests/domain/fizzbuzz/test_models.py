from dataclasses import FrozenInstanceError

import pytest

from src.domain.fizzbuzz.exceptions import (
    EmptyStringException,
    InvalidLimitException,
    ZeroDivisorException,
)
from src.domain.fizzbuzz.models import FizzBuzzParams


class TestFizzBuzzParams:
    def test_int1_zero_raises_exception(self) -> None:
        with pytest.raises(ZeroDivisorException, match="int1 cannot be zero"):
            FizzBuzzParams(int1=0, int2=5, limit=10, str1="Fizz", str2="Buzz")

    def test_int2_zero_raises_exception(self) -> None:
        with pytest.raises(ZeroDivisorException, match="int2 cannot be zero"):
            FizzBuzzParams(int1=3, int2=0, limit=10, str1="Fizz", str2="Buzz")

    def test_valid_params(self) -> None:
        params = FizzBuzzParams(int1=3, int2=5, limit=15, str1="Fizz", str2="Buzz")
        assert params.int1 == 3
        assert params.int2 == 5
        assert params.limit == 15
        assert params.str1 == "Fizz"
        assert params.str2 == "Buzz"

    def test_params_immutable(self) -> None:
        params = FizzBuzzParams(int1=3, int2=5, limit=15, str1="Fizz", str2="Buzz")
        with pytest.raises(FrozenInstanceError):
            params.int1 = 4  # type: ignore

    def test_limit_zero_raises_exception(self) -> None:
        with pytest.raises(InvalidLimitException, match="limit must be positive"):
            FizzBuzzParams(int1=3, int2=5, limit=0, str1="Fizz", str2="Buzz")

    def test_limit_negative_raises_exception(self) -> None:
        with pytest.raises(InvalidLimitException, match="limit must be positive"):
            FizzBuzzParams(int1=3, int2=5, limit=-5, str1="Fizz", str2="Buzz")

    def test_str1_empty_raises_exception(self) -> None:
        with pytest.raises(EmptyStringException, match="str1 cannot be empty"):
            FizzBuzzParams(int1=3, int2=5, limit=10, str1="", str2="Buzz")

    def test_str2_empty_raises_exception(self) -> None:
        with pytest.raises(EmptyStringException, match="str2 cannot be empty"):
            FizzBuzzParams(int1=3, int2=5, limit=10, str1="Fizz", str2="")
