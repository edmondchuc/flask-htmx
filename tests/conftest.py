import pytest
from flask import Flask

from flask_htmx import HTMX
from flask_htmx.responses import HTMXResponseClientRedirect, HTMXResponseStopPolling


@pytest.fixture(scope="function")
def client():
    app = Flask(__name__)
    app.config["TESTING"] = True
    htmx = HTMX(app)

    @app.route("/hx-boost")
    def hx_boost():
        return str(htmx.boosted)

    @app.route("/hx-current-url")
    def hx_current_url():
        return str(htmx.current_url)

    @app.route("/hx-history-restore-request")
    def hx_history_restore_request():
        return str(htmx.history_restore_request)

    @app.route("/hx-prompt")
    def hx_prompt():
        return str(htmx.prompt)

    @app.route("/hx-request")
    def hx_request():
        return str(bool(htmx))

    @app.route("/hx-target")
    def hx_target():
        return str(htmx.target)

    @app.route("/hx-trigger-name")
    def hx_trigger_name():
        return str(htmx.trigger_name)

    @app.route("/hx-trigger")
    def hx_trigger():
        return str(htmx.trigger)

    @app.route("/hx-redirect")
    def hx_redirect():
        return HTMXResponseClientRedirect("/redirected-url")

    @app.route("/hx-trigger-stop-polling")
    def hx_trigger_stop_polling():
        return HTMXResponseStopPolling()

    with app.test_client() as client:
        yield client
