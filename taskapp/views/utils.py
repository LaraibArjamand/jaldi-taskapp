from typing import Optional

from taskapp.models import User

from ..app import bcrypt


def response_message(message: str) -> dict:
    return {"response": message}


def validate_user_input(username: Optional[str], password: Optional[str]) -> Optional[tuple]:
    if username is None:
        return response_message("Username cannot be empty"), 400
    if password is None:
        return response_message("Password cannot be empty"), 400


def validate_user_details(user: User, password: bool) -> bool:
    if not user:
        return response_message("Invalid username")
    
    valid_password = bcrypt.check_password_hash(user.password, password)
    if not user and not valid_password:
        return response_message("Invalid username and password"), 400
    if not valid_password:
        return response_message("Invalid password")


def validate_task_info(title: Optional[str]) -> Optional[tuple]:
    if not title:
        return response_message("Task title cannot be empty"), 400
