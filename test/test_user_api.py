from exception.invalid_token import InvalidToken
from app import app, session, User
from common.common import make_token
import json
import pytest


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture(scope="session")
def user():
    email = "email@gmail.com"
    token = "token"
    name = "HyeonKu Kang22"
    bio = "bio"
    image_url = "https://avatars3.githubusercontent.com/u/11402853?s=460&v=4"
    password = "password"
    user = User(email, password, token, name, bio, image_url)

    session.add(user)
    session.commit()

    return user


def test_client(client):
    response = client.get("/")
    assert b"hello world" == response.data


@pytest.fixture(scope="session", autouse=True)
def user():
    email = "email@gmail.com"
    name = "HyeonKu Kang22"
    password = "password"
    user = User(email=email,
                password=password,
                username=name,
                token=make_token())

    session.add(user)
    session.commit()

    return user


def test_register_user(client):
    data = json.dumps({
        "user": {
            "email": "email@gmail.com",
            "password": "password",
            "username": "hyeonku"
        }
    })
    response = client.post("/users", data=data, content_type="application/json")
    assert response.status_code == 200

    data_dict = response.get_json()
    assert "email" in data_dict
    assert "username" in data_dict
    assert "bio" in data_dict
    assert "image" in data_dict
    assert "token" in data_dict
    assert data_dict["token"] != ""


def test_me(client, user):
    assert user.token is not None
    assert "" != user.token

    response = client.get("/user", headers={"Authorization": f"Token {user.token}"}, content_type="application/json")
    assert response.status_code == 200

    data_dict = response.get_json()

    assert "email" in data_dict
    assert "username" in data_dict
    assert "bio" in data_dict
    assert "image" in data_dict
    assert "token" in data_dict
    assert data_dict["token"] != ""


def test_invalid_token(client):
    response = client.get("/user", headers={"Authorization": ""}, content_type="application/json")
    assert response.status_code == 401

    data_dict = response.get_json()
    assert "message" in data_dict
    assert InvalidToken.message == data_dict["message"]
