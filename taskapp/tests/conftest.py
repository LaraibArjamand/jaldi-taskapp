import json

import pytest
import requests

from ..config import TestConfig

config = TestConfig()


@pytest.fixture
def headers():
    return {
        'Content-Type': 'application/json'
    }


@pytest.fixture
def session():
    session = requests.Session()
    return session


@pytest.fixture
def user_payload():
    return json.dumps({
        "username": config.TEST_USER,
        "password": config.TEST_PASSWORD
    })


@pytest.fixture
def task_payload():
    return json.dumps({
        "title": "Study",
        "description": "Chemistry",
        "is_complete": False
    })


@pytest.fixture
def user_register_session(headers, session, user_payload):
    session.post(config.REGISTER_ENDPOINT, headers=headers, data=user_payload)
    yield session
    # clean up db
    delete_user = json.dumps({"username": config.TEST_USER})
    session.delete(config.LOGIN_ENDPOINT, headers=headers, data=delete_user)


@pytest.fixture
def user_login_session(headers, user_payload, user_register_session):
    user_register_session.post(config.LOGIN_ENDPOINT, headers=headers, data=user_payload)
    return user_register_session


@pytest.fixture
def user_session_with_tasks(headers, user_login_session):
    yield user_login_session

    response = user_login_session.get(config.TASK_ENDPOINT, headers=headers)
    task_ids = [json.loads(task)["id"] for task in response.json()]
    for task_id in task_ids:
        user_login_session.delete(f"{config.TASK_ENDPOINT}/{task_id}", headers=headers)
