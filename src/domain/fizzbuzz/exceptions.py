class FizzBuzzException(Exception):
    pass


class InvalidParametersException(FizzBuzzException):
    pass


class ZeroDivisorException(InvalidParametersException):
    pass


class EmptyStringException(InvalidParametersException):
    pass


class InvalidLimitException(InvalidParametersException):
    pass
