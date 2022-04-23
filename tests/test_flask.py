"""
Flask testing
https://flask.palletsprojects.com/en/2.1.x/testing/
"""
import pytest

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is not None:
        app.config.from_mapping(test_config)

    @app.route("/hallo")
    def hallo():
        return "Hallo, Welt!"

    return app


def test_app_exists():
    assert create_app()


def test_config():
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def client(app):
    return app.test_client()


def test_hallo(client):
    response = client.get("/hallo")
    assert response.status_code == 200
    assert b"Hallo, Welt!" in response.data
