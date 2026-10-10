import pytest

from src.domain.fizzbuzz.models import FizzBuzzParams
from src.domain.fizzbuzz.service import FizzBuzzService


class TestFizzBuzzService:
    def test_multiple_of_int1_replaced_by_str1(self) -> None:
        service = FizzBuzzService()
        params = FizzBuzzParams(int1=3, int2=5, limit=15, str1="Fizz", str2="Buzz")
        result = service.generate(params)
        assert result[2] == "Fizz"
        assert result[5] == "Fizz"
        assert result[8] == "Fizz"

    def test_multiple_of_int2_replaced_by_str2(self) -> None:
        service = FizzBuzzService()
        params = FizzBuzzParams(int1=3, int2=5, limit=15, str1="Fizz", str2="Buzz")
        result = service.generate(params)
        assert result[4] == "Buzz"
        assert result[9] == "Buzz"

    def test_multiple_of_both_replaced_by_str1_str2(self) -> None:
        service = FizzBuzzService()
        params = FizzBuzzParams(int1=3, int2=5, limit=30, str1="Fizz", str2="Buzz")
        result = service.generate(params)
        assert result[14] == "FizzBuzz"
        assert result[29] == "FizzBuzz"

    def test_regular_numbers_stay_as_strings(self) -> None:
        service = FizzBuzzService()
        params = FizzBuzzParams(int1=3, int2=5, limit=10, str1="Fizz", str2="Buzz")
        result = service.generate(params)
        assert result[0] == "1"
        assert result[1] == "2"
        assert result[3] == "4"

    def test_standard_fizzbuzz_sequence(self) -> None:
        service = FizzBuzzService()
        params = FizzBuzzParams(int1=3, int2=5, limit=15, str1="Fizz", str2="Buzz")
        result = service.generate(params)
        expected = [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz",
        ]
        assert result == expected

    def test_custom_parameters(self) -> None:
        service = FizzBuzzService()
        params = FizzBuzzParams(int1=2, int2=3, limit=10, str1="A", str2="B")
        result = service.generate(params)
        expected = [
            "1",
            "A",
            "B",
            "A",
            "5",
            "AB",
            "7",
            "A",
            "B",
            "A",
        ]
        assert result == expected

    def test_result_length_equals_limit(self) -> None:
        for limit in [1, 10, 50, 100]:
            service = FizzBuzzService()
            params = FizzBuzzParams(
                int1=3, int2=5, limit=limit, str1="Fizz", str2="Buzz"
            )
            result = service.generate(params)
            assert len(result) == limit

    def test_int1_equals_int2(self) -> None:
        service = FizzBuzzService()
        params = FizzBuzzParams(int1=3, int2=3, limit=9, str1="A", str2="B")
        result = service.generate(params)
        expected = ["1", "2", "AB", "4", "5", "AB", "7", "8", "AB"]
        assert result == expected

    @pytest.mark.parametrize(
        "int1,int2,limit,str1,str2,position,expected",
        [
            (3, 5, 15, "Fizz", "Buzz", 2, "Fizz"),
            (3, 5, 15, "Fizz", "Buzz", 4, "Buzz"),
            (3, 5, 15, "Fizz", "Buzz", 14, "FizzBuzz"),
            (2, 3, 10, "A", "B", 1, "A"),
            (2, 3, 10, "A", "B", 5, "AB"),
        ],
    )
    def test_generate_parametrized(
        self,
        int1: int,
        int2: int,
        limit: int,
        str1: str,
        str2: str,
        position: int,
        expected: str,
    ) -> None:
        service = FizzBuzzService()
        params = FizzBuzzParams(int1=int1, int2=int2, limit=limit, str1=str1, str2=str2)
        result = service.generate(params)
        assert result[position] == expected
