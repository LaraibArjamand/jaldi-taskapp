from flask import Blueprint

from ..models import Task
from .task import TaskItemView, TaskView
from .user import UserLoginView, UserLogoutView, UserRegisterView

user_bp = Blueprint('user', __name__)
task_bp = Blueprint('task', __name__)


# register auth endpoints
user_bp.add_url_rule("/register", view_func=UserRegisterView.as_view("register"))
user_bp.add_url_rule("/login", view_func=UserLoginView.as_view("login"))
user_bp.add_url_rule("/logout", view_func=UserLogoutView.as_view("logout"))


# register task endpoints
task_bp.add_url_rule("/", view_func=TaskView.as_view("task", Task))
task_bp.add_url_rule("/<int:id>", view_func=TaskItemView.as_view("task_item", Task))
