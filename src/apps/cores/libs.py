"""Third-party packages modules."""
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy, Model
from dynaconf import FlaskDynaconf


class CRUDMixin(Model):
    """Mixin that adds convenience methods for CRUD operations."""

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    @classmethod
    def find_by_id(cls, id: int):
        return cls.query.filter_by(id=id).first()

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()


db = SQLAlchemy(model_class=CRUDMixin)
migrate = Migrate()
config = FlaskDynaconf()
