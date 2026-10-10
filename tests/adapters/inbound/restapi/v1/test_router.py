from fastapi.testclient import TestClient

from src.adapters.inbound.restapi.main import app

client = TestClient(app)


class TestFizzBuzzRouter:
    def test_fizzbuzz_endpoint_success(self) -> None:
        response = client.get(
            "/api/v1/fizzbuzz?int1=3&int2=5&limit=15&str1=Fizz&str2=Buzz"
        )
        assert response.status_code == 200
        result = response.json()
        assert isinstance(result, list)
        assert len(result) == 15
        assert result[2] == "Fizz"
        assert result[4] == "Buzz"
        assert result[14] == "FizzBuzz"

    def test_fizzbuzz_endpoint_validation_error(self) -> None:
        response = client.get("/api/v1/fizzbuzz?int1=0&int2=5&limit=10&str1=F&str2=B")
        assert response.status_code == 400
