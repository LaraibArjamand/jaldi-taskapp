from flask import Blueprint, request
from flask.views import MethodView
from flask_login import current_user

from ..app import db, login_manager
from ..models import Task, User
from .utils import response_message, validate_task_info


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class BaseTaskView:

    def __init__(self, model):
        self.model = model

    def get_task(self, id):
        return self.model.query.filter_by(id=int(id), user_id=current_user.id).first_or_404()


class TaskItemView(MethodView, BaseTaskView):

    def get(self, id):
        if current_user.is_authenticated:
            task = self.get_task(id)
            return task.to_json()
        return response_message("ERROR: You are not logged in"), 401

    def patch(self, id):
        if current_user.is_authenticated:
            task = self.get_task(id)
            task.update_from_json(request.json)
            db.session.commit()
            return task.to_json()
        return response_message("ERROR: You are not logged in"), 401

    def delete(self, id):
        if current_user.is_authenticated:
            task = self.get_task(id)
            db.session.delete(task)
            db.session.commit()
            return "", 204
        return response_message("ERROR: You are not logged in"), 401


class TaskView(MethodView, BaseTaskView):

    def get(self):
        if current_user.is_authenticated:
            tasks = self.model.query.filter_by(user_id=current_user.id).all()
            return [task.to_json() for task in tasks]
        return response_message("ERROR: You are not logged in"), 401

    def post(self):
        if current_user.is_authenticated:
            data = request.json
            if response := validate_task_info(data.get("title")):
                return response
            
            task = Task(
                title=data.get("title"),
                description=data.get("description"),
                is_complete=data.get("is_complete"),
                user_id=current_user.id
            )
            db.session.add(task)
            db.session.commit()
            return task.to_json()
        return response_message("ERROR: You are not logged in"), 401
