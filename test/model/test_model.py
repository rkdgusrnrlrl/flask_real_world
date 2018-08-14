from model.user import User


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
    user = User(email, password, name, token, bio, image_url)

    assert user.email == email
    assert user.token == token
    assert user.username == name
    assert user.bio == bio
    assert user.image == image_url

def test_make_user2():
    email = "email@gmail.com"
    name = "HyeonKu Kang"
    password ="password"
    user = User(email=email, password=password, username=name)

    assert user.email == email
    assert user.username == name

def test_find_user(session, user):
    some_user = session.query(User).filter_by(email="email@gmail.com").first()
    assert user is some_user

import bcrypt

def test_password_should_be_encrypto():
    email = "email@gmail.com"
    token = "token"
    name = "HyeonKu Kang"
    bio = "bio"
    image_url = "https://avatars3.githubusercontent.com/u/11402853?s=460&v=4"
    password = "password"
    user = User(email, password, token, name, bio, image_url)

    assert user.password is not password
    assert bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8"))

def test_check_byte():
    some = b"hwllo"
    assert type(b"") == type(some)