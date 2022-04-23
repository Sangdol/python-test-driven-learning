"""
Flask testing
https://flask.palletsprojects.com/en/2.1.x/testing/
"""
import pytest

from flask import Flask, request, make_response

from werkzeug.exceptions import abort


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is not None:
        app.config.from_mapping(test_config)

    @app.route("/hallo")
    def hallo():
        return "Hallo, Welt!"

    @app.route("/args")
    def args():
        # request.args is a dict
        return request.args["name"]

    @app.route("/abort-400")
    def abort_400():
        # https://stackoverflow.com/questions/21294889/how-to-get-access-to-error-message-from-abort-command-when-using-custom-error-ha
        abort(400, description="Massage in HTML")

    @app.route("/abort-400-plain-text")
    def abort_400_plain_text():
        response = make_response("Something is missing.")
        response.status_code = 400
        abort(response)

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


def test_args(client):
    response = client.get("/args?name=test")
    assert response.status_code == 200
    assert b"test" in response.data


def test_abort(client):
    response = client.get("/abort-400")
    assert response.status_code == 400
    assert b"Massage in HTML" in response.data

    response = client.get("/abort-400-plain-text")
    assert response.status_code == 400
    assert b"Something is missing." == response.data
