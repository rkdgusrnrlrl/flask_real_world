from common.common import make_token

def test_make_token():
    some = make_token()
    assert type("") == type(some)
    assert "" != some