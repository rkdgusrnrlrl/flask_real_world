from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.user import Base, User
from common.common import make_token

app = Flask(__name__)

engine = create_engine('sqlite:///realworld.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()


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