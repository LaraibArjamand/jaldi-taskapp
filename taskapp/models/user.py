import json

from flask_login import UserMixin

from ..app import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"{self.id} - {self.username}"

    def to_json(self):
        return json.dumps({
            "id": self.id,
            "username": self.username,
        })
