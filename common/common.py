import bcrypt
import base64
import hashlib

def ecrypto_password(password):
    hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )
    return hash