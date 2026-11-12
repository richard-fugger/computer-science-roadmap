class JsonValidatorError(Exception):
    pass

class JsonFileReadError(JsonValidatorError):
    pass

class InvalidJsonError(JsonValidatorError):
    pass