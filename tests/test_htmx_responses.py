import pytest
from flask.testing import FlaskClient

from flask_htmx.responses import make_response


def test_htmx_response_client_redirect(client: FlaskClient):
    rv = client.get("/hx-redirect")
    assert rv.headers.get("HX-Redirect") == "/redirected-url"
    assert rv.status_code == 200


def test_htmx_response_stop_polling(client: FlaskClient):
    rv = client.get("/hx-trigger-stop-polling")
    assert rv.status_code == 286

@pytest.mark.parametrize(
    "body, data",
    [
        (
            {},
            {
                "HX-Location": (None, None),
                "HX-Push-Url": (None, None),
                "HX-Redirect": (None, None),
                "HX-Refresh": (None, None),
                "HX-Replace-Url": (None, None),
                "HX-Reswap": (None, None),
                "HX-Retarget": (None, None),
                "HX-Trigger": (None, None),
                "HX-Trigger-After-Settle": (None, None),
                "HX-Trigger-After-Swap": (None, None),
            },
        ),
        (
            {"foo": "bar"},
            {
                "HX-Location": ("/test", "/test"),
                "HX-Push-Url": ("http://google.com", "http://google.com"),
                "HX-Redirect": ("/baz", "/baz"),
                "HX-Refresh": (None, None),
                "HX-Replace-Url": ("http://yahoo.com", "http://yahoo.com"),
                "HX-Reswap": ("outerHTML", "outerHTML"),
                "HX-Retarget": ("#idname", "#idname"),
                "HX-Trigger": ("event", "event"),
                "HX-Trigger-After-Settle": ("event2", "event2"),
                "HX-Trigger-After-Swap": ("event3", "event3"),
            },
        ),
        (
            "foo",
            {
                "HX-Location": (
                    {"path": "/test2", "target": "#testdiv"},
                    '{"path": "/test2", "target": "#testdiv"}',
                ),
                "HX-Push-Url": (False, "false"),
                "HX-Redirect": (None, None),
                "HX-Refresh": (True, "true"),
                "HX-Replace-Url": (False, "false"),
                "HX-Reswap": ("none", "none"),
                "HX-Retarget": (None, None),
                "HX-Trigger": (
                    {"showMessage": "Here Is A Message"},
                    '{"showMessage": "Here Is A Message"}',
                ),
                "HX-Trigger-After-Settle": (
                    {
                        "showMessage": {
                            "level": "info",
                            "message": "Here Is A Message",
                        }
                    },
                    '{"showMessage": {"level": "info", "message": "Here Is A Message"}}',  # noqa
                ),
                "HX-Trigger-After-Swap": (
                    {"event1": "A message", "event2": "Another message"},
                    '{"event1": "A message", "event2": "Another message"}',
                ),
            },
        ),
    ],
)
def test_make_response(flask_app, body, data):
    mapping = {
        "location": "HX-Location",
        "push_url": "HX-Push-Url",
        "redirect": "HX-Redirect",
        "refresh": "HX-Refresh",
        "replace_url": "HX-Replace-Url",
        "reswap": "HX-Reswap",
        "retarget": "HX-Retarget",
        "trigger": "HX-Trigger",
        "trigger_after_settle": "HX-Trigger-After-Settle",
        "trigger_after_swap": "HX-Trigger-After-Swap",
    }
    kwargs = {key: data[header][0] for key, header in mapping.items()}
    kwargs = {k: v for k, v in kwargs.items() if v is not None}
    with flask_app.app_context():
        resp = make_response(body, **kwargs)
    for header, value in data.items():
        if value[0] is None:
            assert header not in resp.headers
        else:
            assert value[1] == resp.headers[header]


def test_make_response_invalid_reswap(flask_app):
    with flask_app.app_context():
        with pytest.raises(ValueError):
            make_response("body", reswap="invalid_reswap")
