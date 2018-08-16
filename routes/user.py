from flask import Blueprint, request, jsonify, g
from model.user import User
from common.common import make_token, check_password
from common.annotaion import token_need
from exception import InvalidUsage
from extensions import db

blueprint = Blueprint('user', __name__)


@blueprint.route("/")
def index():
    return "hello world"


@blueprint.route("/users", methods=["POST"])
def register_user():
    payload = request.get_json()["user"]

    user = User(email=payload["email"],
                password=payload["password"],
                username=payload["username"],
                token=make_token())

    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict())


@blueprint.route("/user", methods=["GET"])
@token_need
def about_me():
    return jsonify(g.user.to_dict())


@blueprint.route("/user", methods=["PUT"])
@token_need
def update_me():
    user_dict = request.get_json()["user"]
    user = g.user

    db.session.query(User).filter_by(email=user.email).update(user_dict)
    db.session.commit()

    return jsonify(dict({"user" : g.user.to_dict()}))


@blueprint.route("/users/login", methods=["POST"])
def login():
    payload = request.get_json()["user"]
    password = payload['password']
    user = db.session.query(User).filter_by(email=payload["email"]).first()
    if not check_password(password, user.password):
        raise InvalidUsage.user_not_found()

    return jsonify(user.to_dict())
