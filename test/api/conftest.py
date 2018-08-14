import pytest
from app import app, session, User
from common.common import make_token

@pytest.fixture
def client():
    return app.test_client()


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