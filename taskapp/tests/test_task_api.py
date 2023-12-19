import json

import pytest

from .conftest import TASK_ENDPOINT


@pytest.fixture
def create_task_id(headers, task_payload, user_session_with_tasks):
    create_response = user_session_with_tasks.post(TASK_ENDPOINT, headers=headers, data=task_payload)
    return create_response.json()["id"]


def test_task_create(headers, task_payload, user_session_with_tasks):
    create_response = user_session_with_tasks.post(TASK_ENDPOINT, headers=headers, data=task_payload)
    assert create_response.status_code == 200

    new_task = create_response.json()

    # Verify the created task matches the payload
    new_task = create_response.json()
    task_payload = json.loads(task_payload)
    assert all(new_task[prop] == task_payload[prop] for prop in task_payload)

    # Verify the created task is present in the list of all tasks
    list_response = user_session_with_tasks.get(TASK_ENDPOINT, headers=headers)
    tasks_list = [json.loads(task) for task in list_response.json()]
    assert new_task in tasks_list


def test_task_update(headers, user_session_with_tasks, create_task_id):
    update_data = {
        "is_complete": True 
    }
    update_response = user_session_with_tasks.patch(f"{TASK_ENDPOINT}/{create_task_id}", headers=headers, json=update_data)
    updated_task = update_response.json()

    assert updated_task["is_complete"] == update_data["is_complete"]


def test_task_delete(headers, user_session_with_tasks, create_task_id):
    user_session_with_tasks.delete(f"{TASK_ENDPOINT}/{create_task_id}")

    # Verify the created task is not present in the list of all tasks
    list_response = user_session_with_tasks.get(TASK_ENDPOINT, headers=headers)
    tasks_list = [json.loads(task)["id"] for task in list_response.json()]
    assert create_task_id not in tasks_list


