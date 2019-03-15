from datetime import datetime

from flask import jsonify
from dynaconf import settings
from werkzeug.exceptions import (
    NotFound as _NotFound,
    UnprocessableEntity as _UnprocessableEntity,
)


def register_error_handlers(app):
    def err_response(error):
        return error.to_json(), error.code

    def handle_err(error):
        if type(error) is _NotFound:
            return err_response(NotFound())

        if type(error) is _UnprocessableEntity:
            return err_response(UnprocessableEntity(error=error))

        if isinstance(error, BaseError):
            return err_response(error)

        return err_response(InternalServerError())

    app.errorhandler(Exception)(handle_err)


def err_template(code, message):
    timestamp_format = settings.get('FULL_DATETIME')
    return {
        'response': {
            'error_code': code,
            'error_message': message,
            'request_id': 1234,  # TODO: change me
            'timestamp': datetime.utcnow().strftime(timestamp_format)
        }
    }


class BaseError(Exception):

    def __init__(self, code=500, message='', payload=None):
        Exception.__init__(self)
        self.code = code
        self.message = message
        self.payload = payload

    def to_json(self):
        res_body = err_template(code=self.code, message=self.message)
        return jsonify(res_body)


class BadRequest(BaseError):
    def __init__(self, message='Bad request.'):
        super().__init__(code=400, message=message)


class Unauthorized(BaseError):
    def __init__(self, message='Unauthorized.'):
        super().__init__(code=401, message=message)


class Forbidden(BaseError):
    def __init__(self, message='Forbidden'):
        super().__init__(code=403, message=message)


class NotFound(BaseError):
    def __init__(self, message='Not found.'):
        super().__init__(code=404, message=message)


class MethodNotAllow(BaseError):
    def __init__(self, message='This method is not allowed.'):
        super().__init__(code=405, message=message)


class InternalServerError(BaseError):
    def __init__(self, message='Internal server error.'):
        super().__init__(code=500, message=message)


class UnprocessableEntity(BaseError):
    def __init__(self, error=None):
        super().__init__(code=400)
        self.message = error.description
