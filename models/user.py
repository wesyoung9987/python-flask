import sqlite3
from db import db
from flask_bcrypt import generate_password_hash

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    pw_hash = db.Column(db.String(120))

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password, 12)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
