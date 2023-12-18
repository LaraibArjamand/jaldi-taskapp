from flask import request
from flask.views import MethodView
from flask_login import current_user

from ..app import db, login_manager
from ..models import Task, User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class TaskItemView(MethodView):

    def __init__(self, model):
        self.model = model

    def _get_item(self, id):
        return self.model.query.filter_by(id=id, user_id=current_user.id).first_or_404()

    def get(self, id):
        if current_user.is_authenticated:
            task = self._get_item(id)
            return task.to_json()
        return {"message": "You need to login first"}

    def patch(self, id):
        if current_user.is_authenticated:
            task = self._get_item(id)
            task.update_from_json(request.json)
            db.session.commit()
            return task.to_json()
        return {"message": "You need to login first"}

    def delete(self, id):
        if current_user.is_authenticated:
            task = self._get_item(id)
            db.session.delete(task)
            db.session.commit()
            return "", 204
        return {"message": "You need to login first"}


class TaskView(MethodView):

    def __init__(self, model):
        self.model = model

    def get(self):
        if current_user.is_authenticated:
            tasks = self.model.query.filter_by(user_id=current_user.id).all()
            return [task.to_json() for task in tasks]
        return {"message": "You need to login first"}

    def post(self):
        if current_user.is_authenticated:
            data = request.json
            task = Task(
                title=data.get("title"),
                description=data.get("description"),
                is_complete=data.get("is_complete"),
                user_id=current_user.id
            )
            db.session.add(task)
            db.session.commit()
            return task.to_json()
        return {"message": "You need to login first"}
