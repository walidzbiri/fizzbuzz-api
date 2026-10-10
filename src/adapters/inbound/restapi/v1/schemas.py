from pydantic import BaseModel, Field, RootModel


class FizzBuzzParams(BaseModel):
    int1: int = Field(..., description="First integer for FizzBuzz")
    int2: int = Field(..., description="Second integer for FizzBuzz")
    limit: int = Field(..., description="Limit for FizzBuzz sequence")
    str1: str = Field(min_length=1, description="String to replace multiples of int1")
    str2: str = Field(min_length=1, description="String to replace multiples of int2")


class FizzBuzzResponse(RootModel[list[str]]):
    root: list[str] = Field(..., description="FizzBuzz sequence")


class FizzBuzzStatsResponse(BaseModel):
    int1: int
    int2: int
    limit: int
    str1: str
    str2: str
    hits: int
