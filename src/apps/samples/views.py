from flask_restplus import Api
from flask import Blueprint, abort, jsonify, request

from src.apps.cores.exceptions import (
    register_error_handlers,
    NotFound,
    UnprocessableEntity,
)
from src.apps.cores.views import BaseView
from .models import Sample
from .schemas import sample_schema


blueprint = Blueprint('sample', __name__)
api = Api(blueprint, doc='/doc/')
register_error_handlers(api)


@api.route('/')
class Index(BaseView):
    def get(self):
        raise NotFound('custom message.')
        return jsonify({
            'samples': [sample.title for sample in Sample.query.all()]
        })


@api.route('/new')
class New(BaseView):
    def post(self):
        request_data = request.get_json()
        data, errors = sample_schema.load(request_data)
        if errors:
            raise UnprocessableEntity(errors)
        Sample.create(title=data.get('title'), body=data.get('body'))
        return 201


@api.route('/get/<string:sample_id>')
class Get(BaseView):
    def get(self, sample_id):
        sample = Sample.find_by_id(int(sample_id))
        if not sample:
            abort(404, 'not found')
        return self.render_json_response(sample, status_code=200, schema=sample_schema)


@api.route('/update/<string:sample_id>')
class Update(BaseView):
    def post(self, sample_id):
        title = request.form.get('title')
        body = request.form.get('body')

        # TODO: protect mass assignment

        sample = Sample.find_by_id(int(sample_id))
        if not sample:
            abort(404, 'not found')

        sample_updated = sample.update(title=title, body=body)
        return self.render_json_response(sample_updated, status_code=200, schema=sample_schema)


@api.route('/delete/<string:sample_id>')
class Delete(BaseView):
    def delete(self, sample_id):
        sample = Sample.find_by_id(int(sample_id))
        if not sample:
            abort(404, 'not found')

        sample.delete()
        return {'message': 'sample {} is deleted'.format(sample.id)}
