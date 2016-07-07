class RadioException(Exception):
    def __init__(self, error_code, message):
        Exception.__init__(self)
        self.error_code = error_code
        self.message = message

    def to_dict(self):
        rv = {}
        rv['error_code'] = self.error_code
        rv['message'] = self.message
        return rv
