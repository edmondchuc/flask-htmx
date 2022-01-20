from flask import Flask

from flask_htmx import HTMX


def test_init_app():
    app = Flask(__name__)
    htmx = HTMX()
    htmx.init_app(app)
    assert hasattr(app, "htmx")
    assert type(app.htmx) == HTMX


def test_init_app_via_constructor():
    app = Flask(__name__)
    HTMX(app)
    assert hasattr(app, "htmx")
    assert type(app.htmx) == HTMX
