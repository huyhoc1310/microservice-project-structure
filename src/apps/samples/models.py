from ..cores.libs import db


class Sample(db.Model):
    __tablename__ = 'samples'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.String(255))

    def __init__(self, title: str, body: str):
        db.Model.__init__(self, title=title, body=body)

    def __repr__(self):
        return f'<Sample: \'{self.title}\'>'
