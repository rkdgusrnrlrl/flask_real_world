from common.common import make_token
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
