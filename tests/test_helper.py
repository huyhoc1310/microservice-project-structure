from flask_testing import TestCase
from src.app import create_app
from src.apps.cores.libs import db


class BaseTestCase(TestCase):

    def create_app(self):
        app = create_app()
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
