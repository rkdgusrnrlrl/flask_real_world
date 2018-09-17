from model.user import User
from extensions import db
from settings import TestConfig
import pytest


@pytest.fixture(scope="class")
def session():
    db.init_engine(TestConfig)
    db.init_model()
    yield db.session
    db.session.remove()


@pytest.fixture(scope="function")
def user(session):
    email = "email@gmail.com"
    token = "token"
    name = "HyeonKu Kang"
    bio = "bio"
    image_url = "https://avatars3.githubusercontent.com/u/11402853?s=460&v=4"
    password = "password"
    user = User(email, password, name, token, bio, image_url)

    session.add(user)
    yield user
    session.rollback()
