from flask_restplus import Api, Resource
from flask import Blueprint, abort, jsonify, request

from .models import Sample


blueprint = Blueprint('sample', __name__)
api = Api(blueprint, doc='/doc/')


@api.route('/')
class Index(Resource):
    def get(self):
        return jsonify({
            'samples': [sample.title for sample in Sample.query.all()]
        })


@api.route('/new')
class New(Resource):
    def post(self):
        title = request.form.get('title')
        body = request.form.get('body')

        if not title or not body:
            abort(400, 'bad request')

        Sample.create(title=title, body=body)
        return 200


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
