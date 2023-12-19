from .conftest import config


def test_user_register(session, user_payload, headers):
    response = session.post(config.REGISTER_ENDPOINT, headers=headers, data=user_payload)
    assert response.status_code == 201

    response = session.post(config.LOGIN_ENDPOINT, headers=headers, data=user_payload)
    assert response.status_code == 200


def test_user_login(user_register_session, user_payload, headers):
    response = user_register_session.post(config.LOGIN_ENDPOINT, headers=headers, data=user_payload)
    assert response.status_code == 200


def test_user_logout(user_login_session, user_payload, headers):
    response = user_login_session.post(config.LOGOUT_ENDPOINT, headers=headers, data=user_payload)
    assert response.status_code == 200
