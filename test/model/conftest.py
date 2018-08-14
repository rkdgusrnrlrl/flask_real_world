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
    session.commit()

    return user
