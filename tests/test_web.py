import pytest
import json

from src.web import app as flask_app
from mylib.mkchange import change

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index(app, client):
    result = client.get("/")
    assert result.status_code == 200
    assert {"hello": "jkuffor"} == json.loads(result.get_data(as_text=True))
    
def test_change(app, client):
    result = client.get("/change/1/35")
    assert result.status_code == 200
    assert [{'5': 'quarters'}, {'1': 'dimes'}] == json.loads(result.get_data(as_text=True))
