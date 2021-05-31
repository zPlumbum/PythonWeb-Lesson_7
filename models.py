import hashlib

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import exc

from main import app


SALT = 'qwerty'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class BaseModelMixin:

    @classmethod
    def by_id(cls, obj_id):
        obj = cls.query.get(obj_id)
        if obj:
            return obj
        else:
            pass

    def add(self):
        db.session.add(self)
        try:
            db.session.commit()
        except exc.IntegrityError as ex:
            print(ex)

    def delete(self):
        db.session.delete(self)
        try:
            db.session.commit()
        except exc.IntegrityError as ex:
            print(ex)


class User(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __str__(self):
        return f'User {self.username}'

    def __repr__(self):
        return str(self)

    def set_password(self, raw_password):
        raw_password = f'{raw_password}{SALT}'
        self.password = hashlib.md5(raw_password.encode()).hexdigest()

    def check_password(self, raw_password):
        raw_password = f'{raw_password}{SALT}'
        return self.password == hashlib.md5(raw_password.encode()).hexdigest()

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            "email": self.email
        }


db.create_all(app=app)
