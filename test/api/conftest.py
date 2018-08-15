import pytest
from app import create_app
from settings import TestConfig, DevConfig
from common.common import make_token
from extensions import db
from model.user import User

@pytest.fixture(scope="class")
def client():
    app = create_app(DevConfig)
    yield app.test_client()
    db.session.remove()


@pytest.fixture(scope="function")
def user(client):
    email = "email@gmail.com"
    name = "HyeonKu Kang22"
    password = "password"
    user = User(email=email,
                password=password,
                username=name,
                token=make_token())

    db.session.add(user)
    yield user
    db.session.rollback()