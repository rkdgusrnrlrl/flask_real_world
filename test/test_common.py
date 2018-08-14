from common.common import make_token, check_password, ecrypto_password
import re


def test_make_token():
    some = make_token()
    assert type("") == type(some)
    assert "" != some


def test_regex():
    auth = "Token 123"
    regex = re.compile(r"^Token ([a-z0-9]+)")
    match = regex.search(auth)

    assert match is not None

    token = match.group(1)
    assert token == "123"


def test_check_password():
    raw = "password"
    hashed = ecrypto_password(raw)

    assert check_password(raw, hashed)
