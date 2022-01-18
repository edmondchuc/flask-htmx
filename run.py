from flask import Flask, render_template
from flask_htmx import HTMX

app = Flask(__name__)
htmx = HTMX()
htmx.init_app(app)


@app.route("/")
def home():
    print("Home route.")
    if htmx:
        print("It was a HTMX request.")
    else:
        print("It was NOT a HTMX request.")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
