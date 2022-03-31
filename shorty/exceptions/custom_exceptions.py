class ShortyException(Exception):
    pass


class BadRequest(ShortyException):
    pass


class APIUnauthorizedError(ShortyException):
    pass


class APIForbiddenError(ShortyException):
    pass


class APINotFoundError(ShortyException):
    pass


class APINotAcceptableError(ShortyException):
    pass


class APIConflictError(ShortyException):
    pass


class APIRequestTooLangeError(ShortyException):
    pass


class APIUnsupportedTypeError(ShortyException):
    pass


class APIUncaughtExceptionError(ShortyException):
    pass


class APINotImplementedError(ShortyException):
    pass


class APIServiceUnavailableError(ShortyException):
    pass


class APIGatewayError(ShortyException):
    pass


class APIGatewayTimeoutError(ShortyException):
    pass
