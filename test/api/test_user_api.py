from exception.invalid_token import InvalidToken
import pytest
import json


def test_client(client):
    response = client.get("/")
    assert b"hello world" == response.data


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
