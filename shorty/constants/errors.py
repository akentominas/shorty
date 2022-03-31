from shorty.exceptions.custom_exceptions import (
    BadRequest,
    APIUnauthorizedError,
    APIForbiddenError,
    APINotFoundError,
    APINotAcceptableError,
    APIConflictError,
    APIRequestTooLangeError,
    APIUnsupportedTypeError,
    APIUncaughtExceptionError,
    APINotImplementedError,
    APIServiceUnavailableError,
    APIGatewayError,
    APIGatewayTimeoutError
)

ERROR_CODES = {
    400: BadRequest,
    401: APIUnauthorizedError,
    403: APIForbiddenError,
    404: APINotFoundError,
    406: APINotAcceptableError,
    409: APIConflictError,
    413: APIRequestTooLangeError,
    415: APIUnsupportedTypeError,
    500: APIUncaughtExceptionError,
    501: APINotImplementedError,
    502: APIGatewayError,
    503: APIServiceUnavailableError,
    504: APIGatewayTimeoutError,
}
