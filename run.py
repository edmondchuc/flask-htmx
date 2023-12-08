from functools import partial
from flask import Flask, render_template
from flask_htmx import HTMX
from flask_htmx.responses import HTMXResponseClientRedirect

app = Flask(__name__)
htmx = HTMX(app)


@app.route("/")
def home():
    if htmx:
        return render_template("partials/thing.html")
    return render_template("index.html")


@app.route("/redirect")
def redirect_route():
    return HTMXResponseClientRedirect("/redirected-endpoint")


@app.route("/redirected-endpoint")
def redirected_endpoint():
    return "You have been redirected to /redirected-endpoint"


if __name__ == "__main__":
    app.run(debug=True)
