from flask_restplus import Resource


class BaseView(Resource):
    def render_json_response(self, obj=None, status_code: int = 200, schema=None, many=False, **kwargs):
        response = dict()
        if obj:
            response.update({
                'result': schema.dump(obj, many=many).data
            })
        response.update(kwargs)
        return response, status_code
