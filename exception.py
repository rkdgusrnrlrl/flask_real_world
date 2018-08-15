from flask import jsonify


def template(data, code=500):
    return {'message': data, 'status_code': code}


USER_NOT_FOUND = template('User not found', code=500)
INVAILD_TOKEN = template('invalid token', code=401)


class InvalidUsage(Exception):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_json(self):
        rv = self.message
        return jsonify({"message" : self.message})

    @classmethod
    def user_not_found(cls):
        return cls(**USER_NOT_FOUND)

    @classmethod
    def invalid_token(cls):
        return cls(**INVAILD_TOKEN)
