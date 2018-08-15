from model.user import User
from functools import wraps
from extensions import db
from exception import InvalidUsage
from flask import request, g
import re


def token_need(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not ("Authorization" in request.headers):
            raise InvalidUsage.invalid_token()

        auth = request.headers.get("Authorization")
        regex = re.compile(r"^Token ([a-z0-9]+)")
        match = regex.search(auth)

        if match is None:
            raise InvalidUsage.invalid_token()

        token = match.group(1)
        user = db.session.query(User).filter_by(token=token).first()
        print(user)

        if user is None:
            raise InvalidUsage.invalid_token()

        g.user = user
        return f(*args, **kwargs)

    return decorated_function
