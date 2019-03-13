from ..cores.libs import db
from marshmallow import Schema, fields, validate


class Sample(db.Model):
    __tablename__ = 'samples'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.String(255))

    def __init__(self, title: str, body: str):
        db.Model.__init__(self, title=title, body=body)

    def __repr__(self):
        return f'<Sample: \'{self.title}\'>'


class SampleSchema(Schema):
    id = fields.Int()
    title = fields.Str(validate=validate.Length(min=1, max=10, error='Max length = 100'), required=True, error_messages={'required': 'Required field'})
    body = fields.Str(validate=validate.Length(max=100, error='Max length = 200'))


sample_schema = SampleSchema(only=('title', 'body'))
samples_schema = SampleSchema(many=True)
