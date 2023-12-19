
import json

from ..app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    is_complete = db.Column(db.Boolean, default=False)

    # assosciate tasks with user
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("tasks", lazy=True))

    def __repr__(self) -> str:
        return f"{self.id} - {self.title}"

    def to_json(self):
        return json.dumps({
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "is_complete": self.is_complete,
        })

    def update_from_json(self, updated_data: dict):
        for prop, value in updated_data.items():
            setattr(self, prop, value)
