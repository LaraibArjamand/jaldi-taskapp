from typing import Optional


def response_message(message: str) -> dict:
    return {"response": message}


def validate_user_info(username: Optional[str], password: Optional[str]) -> Optional[tuple]:
    if username is None:
        return response_message("Username cannot be empty"), 400
    if password is None:
        return response_message("Password cannot be empty"), 400


def validate_task_info(title: Optional[str]) -> Optional[tuple]:
    if title is None:
        return response_message("Task title cannot be empty"), 400