from flask_restplus import Api, Resource
from flask import Blueprint, abort, jsonify, request

from src.apps.cores.exceptions import register_error_handlers, NotFound, UnprocessableEntity
from .models import Sample, sample_schema, samples_schema


blueprint = Blueprint('sample', __name__)
api = Api(blueprint, doc='/doc/')
register_error_handlers(api)


@api.route('/')
class Index(Resource):
    def get(self):
        raise NotFound('custom message.')
        return jsonify({
            'samples': [sample.title for sample in Sample.query.all()]
        })


@api.route('/new')
class New(Resource):
    def post(self):
        request_data = request.get_json()
        data, errors = sample_schema.load(request_data)
        if errors:
            abort(422, errors)
        Sample.create(title=data.get('title'), body=data.get('body'))
        return 201


@api.route('/get/<string:sample_id>')
class Get(Resource):
    def get(self, sample_id):
        sample = Sample.find_by_id(int(sample_id))
        if not sample:
            abort(404, 'not found')

        return {'sample': {
            'title': sample.title,
            'body': sample.body,
        }}


@api.route('/update/<string:sample_id>')
class Update(Resource):
    def post(self, sample_id):
        title = request.form.get('title')
        body = request.form.get('body')

        # TODO: protect mass assignemnt

        sample = Sample.find_by_id(int(sample_id))
        if not sample:
            abort(404, 'not found')

        sample.update(title=title, body=body)
        return 200


@api.route('/delete/<string:sample_id>')
class Delete(Resource):
    def delete(self, sample_id):
        sample = Sample.find_by_id(int(sample_id))
        if not sample:
            abort(404, 'not found')

        sample.delete()
        return {'message': 'sample {} is deleted'.format(sample.id)}
