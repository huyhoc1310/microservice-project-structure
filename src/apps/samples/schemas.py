from marshmallow import Schema, fields, validate

class SampleSchema(Schema):
    id = fields.Int()
    title = fields.Str(
        validate=validate.Length(
            min=1,
            max=10,
            error='Max length = 100 && Min length = 1'
        ),
        required=True, error_messages={'required': 'Required field'}
    )
    body = fields.Str(
        validate=validate.Length(max=100, error='Max length = 200')
    )


sample_schema = SampleSchema(only=('title', 'body'))
samples_schema = SampleSchema(many=True)
