from flask.testing import FlaskClient


def test_htmx_response_client_redirect(client: FlaskClient):
    rv = client.get("/hx-redirect")
    assert rv.headers.get("HX-Redirect") == "/redirected-url"
    assert rv.status_code == 200


def test_htmx_response_stop_polling(client: FlaskClient):
    rv = client.get("/hx-trigger-stop-polling")
    assert rv.status_code == 286
