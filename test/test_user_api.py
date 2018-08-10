from app import app
import json
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_client(client):
    response = client.get("/")
    assert b"hello world" == response.data

def test_register_user(client):
    data = json.dumps({
        "user" : {
            "email" : "email@gmail.com",
            "password" : "password",
            "username" : "hyeonku"
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

