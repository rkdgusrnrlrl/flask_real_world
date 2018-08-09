from app import app
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_client(client):
    response = client.get("/")
    assert b"hello world" == response.data