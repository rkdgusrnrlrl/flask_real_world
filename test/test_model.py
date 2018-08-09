from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.user import User
from model.user import Base
import pytest


@pytest.fixture(scope="session")
def engine():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    return engine

@pytest.fixture(scope="session")
def session(engine):
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()
    return session

@pytest.fixture(scope="session", autouse=True)
def user(session):
    email = "email@gmail.com"
    token = "token"
    name = "HyeonKu Kang"
    bio = "bio"
    image_url = "https://avatars3.githubusercontent.com/u/11402853?s=460&v=4"
    password ="password"
    user = User(email, password, token, name, bio, image_url)

    session.add(user)
    return user


def test_should_be_1(engine):
    some = engine.execute("select 1").scalar()
    assert 1 == some

def test_make_user():
    email = "email@gmail.com"
    token = "token"
    name = "HyeonKu Kang"
    bio = "bio"
    image_url = "https://avatars3.githubusercontent.com/u/11402853?s=460&v=4"
    password ="password"
    user = User(email, password, token, name, bio, image_url)

    assert user.email == email
    assert user.token == token
    assert user.name == name
    assert user.bio == bio
    assert user.image == image_url

def test_find_user(session, user):
    some_user = session.query(User).filter_by(email="email@gmail.com").first()
    assert user is some_user

