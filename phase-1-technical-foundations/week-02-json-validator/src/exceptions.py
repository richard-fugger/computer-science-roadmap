class JsonValidatorException(Exception):
    pass

class JsonFileReadError(JsonValidatorException):
    pass

class InvalidJsonError(JsonValidatorException):
    pass