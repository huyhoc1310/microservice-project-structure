from flask import jsonify
from werkzeug.exceptions import NotFound as _NotFound
from datetime import datetime


def register_errorhandlers(app):
    def err_response(error):
        return error.to_json(), error.code

    def handle_err(error):
        if type(error) is _NotFound:
            return err_response(NotFound())

        if isinstance(error, BaseError):
            return err_response(error)

        return err_response(InternalServerError())

    app.errorhandler(Exception)(handle_err)


def err_template(code, message):
    return {
        'response': {
            'error_code': code,
            'error_message': message,
            'request_id': 1234, # TODO: change me
            'timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
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
    def __init__(self, message='Unauthrozied.'):
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
