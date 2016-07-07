from . import RadioException


class ValidationException(RadioException):
    def __init___(self, error_code, message):
        RadioException.__init__(self, error_code, message)
