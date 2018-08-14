from flask import Flask, request, jsonify, g
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.user import Base, User
from common.common import make_token, check_password
from functools import wraps
from exception.invalid_token import InvalidToken
from exception.not_found_user import NotFoundUser

import re

app = Flask(__name__)

engine = create_engine('sqlite:///realworld.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()


@app.errorhandler(InvalidToken)
def hadle_invalid_token(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(NotFoundUser)
def hadle_not_found_user(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def token_need(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not ("Authorization" in request.headers):
            raise InvalidToken

        auth = request.headers.get("Authorization")
        regex = re.compile(r"^Token ([a-z0-9]+)")
        match = regex.search(auth)

        if match is None:
            raise InvalidToken

        token = match.group(1)
        user = session.query(User).filter_by(token=token).first()
        print(user)

        if user is None:
            raise InvalidToken

        g.user = user
        return f(*args, **kwargs)

    return decorated_function


@app.route("/")
def index():
    return "hello world"


@app.route("/users", methods=["POST"])
def register_user():
    payload = request.get_json()["user"]

    user = User(email=payload["email"],
                password=payload["password"],
                username=payload["username"],
                token=make_token())

    session.add(user)
    session.commit()

    return jsonify(user.to_dict())


@app.route("/user", methods=["GET"])
@token_need
def about_me():
    return jsonify(g.user.to_dict())


@app.route("/users/login", methods=["POST"])
def login():
    payload = request.get_json()["user"]
    password = payload['password']
    user = session.query(User).filter_by(email=payload["email"]).first()
    if not check_password(password, user.password):
        raise NotFoundUser()

    return jsonify(user.to_dict())
