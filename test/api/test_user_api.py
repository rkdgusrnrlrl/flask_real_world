from exception import INVAILD_TOKEN
import json

class TestUserApi(object):
    def test_client(self, client):
        response = client.get("/")
        assert b"hello world" == response.data


    def test_register_user(self, client):
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

    def test_login(self, client, user):
        data = json.dumps({
            "user": {
                "email": user.email,
                "password": "password",
            }
        })
        response = client.post("/users/login", data=data, content_type="application/json")
        assert response.status_code == 200

        data_dict = response.get_json()

        assert "email" in data_dict
        assert "username" in data_dict
        assert "bio" in data_dict
        assert "image" in data_dict
        assert "token" in data_dict
        assert data_dict["token"] != ""


    def test_login_wrong_password_should_be_not_found_user(self, client, user):
        data = json.dumps({
            "user": {
                "email": user.email,
                "password": "password1",
            }
        })
        response = client.post("/users/login", data=data, content_type="application/json")
        assert response.status_code == 500

        data_dict = response.get_json()

        assert "message" in data_dict

    def test_invalid_token(self, client):
        response = client.get("/user", headers={"Authorization": ""}, content_type="application/json")
        assert response.status_code == 401

        data_dict = response.get_json()
        assert "message" in data_dict
        assert INVAILD_TOKEN["message"] == data_dict["message"]

    def test_current_use(self, client, user):
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

    def test_update_user(self, client, user):
        data = json.dumps({
            "user": {
                "email": "new_email@email.com",
            }
        })
        response = client.put("/user",
                              headers={"Authorization": f"Token {user.token}"},
                              content_type="application/json",
                              data=data)
        assert response.status_code == 200

        json_dict = response.get_json()
        assert "user" in json_dict
        
        user_dict = json_dict["user"]
        
        assert "email" in user_dict
        assert "username" in user_dict
        assert "bio" in user_dict
        assert "image" in user_dict
        assert "token" in user_dict
        assert user_dict["token"] != ""

