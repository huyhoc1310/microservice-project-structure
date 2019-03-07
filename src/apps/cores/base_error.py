# encoding: utf-8
"""
Created on 07/03/2019

@author: FRAMGIA\le.quy.quyet
"""

from flask import abort


def _error_abort(code, message):
    error = {
        'code': code,
        'message': message,
    }
    abort(code, error=error)


class BaseError(Exception):
    """Base Error Class"""

    def __init__(self, code=400, message='', status='', field=None):
        Exception.__init__(self)
        self.code = code
        self.message = message
        self.status = status
        self.field = field

    def to_dict(self):
        return {'code': self.code,
                'message': self.message,
                'status': self.status,
                'field': self.field, }


class NotFoundError(BaseError):
    def __init__(self, message='Not found'):
        BaseError.__init__(self)
        self.code = 404
        self.message = message
        self.status = 'NOT_FOUND'


class NotAuthorizedError(BaseError):
    def __init__(self, message='Unauthorized'):
        BaseError.__init__(self)
        self.code = 401
        self.message = message
        self.status = 'NOT_AUTHORIZED'


class ValidationError(BaseError):
    def __init__(self, field, message='Invalid field'):
        BaseError.__init__(self)
        self.code = 400
        self.message = message
        self.status = 'INVALID_FIELD'
        self.field = field

