import json

from .conftest import LOGIN_ENDPOINT, LOGOUT_ENDPOINT, REGISTER_ENDPOINT


def test_user_register(session, user_payload, headers):
    response = session.post(REGISTER_ENDPOINT, headers=headers, data=user_payload)
    assert response.status_code == 201

    response = session.post(LOGIN_ENDPOINT, headers=headers, data=user_payload)
    assert response.status_code == 200


def test_user_login(user_register_session, user_payload, headers):
    response = user_register_session.post(LOGIN_ENDPOINT, headers=headers, data=user_payload)
    assert response.status_code == 200


def test_user_logout(user_login_session, user_payload, headers):
    response = user_login_session.post(LOGOUT_ENDPOINT, headers=headers, data=user_payload)
    assert response.status_code == 200
