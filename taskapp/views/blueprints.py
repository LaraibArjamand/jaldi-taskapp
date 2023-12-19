from flask import Blueprint

from ..models import Task, User
from .authentication import UserLoginView, UserLogoutView, UserRegisterView
from .task import TaskItemView, TaskView

auth_bp = Blueprint('auth', __name__)
task_bp = Blueprint('task', __name__)
# task_item_bp = Blueprint('task_item', __name__)

# register auth endpoints
auth_bp.add_url_rule("/register", view_func=UserRegisterView.as_view("register"))
auth_bp.add_url_rule("/login", view_func=UserLoginView.as_view("login"))
auth_bp.add_url_rule("/logout", view_func=UserLogoutView.as_view("logout"))


# register task endpoints
task_bp.add_url_rule("/", view_func=TaskView.as_view("task", Task))
task_bp.add_url_rule("/<int:id>", view_func=TaskItemView.as_view("task_item", Task))
# task_item_bp.add_url_rule("/task/<int:id>", view_func=TaskItemView.as_view("task-item", Task))
