Quickstart
==========

Install the extension with pip.

.. code-block:: none

    pip install flask-htmx

Or perhaps you use Poetry.

.. code-block:: none

    poetry add flask-htmx

You can register the HTMX object by passing the Flask
:code:`app` object via the constructor.

.. code-block:: python

    htmx = HTMX(app)

Or you can register the HTMX object using
:py:meth:`.HTMX.init_app`.

.. code-block:: python

    htmx = HTMX()
    htmx.init_app(app)

A minimal working example.

.. code-block:: python

    from flask import Flask
    from flask_htmx import HTMX

    app = Flask(__name__)
    htmx = HTMX(app)

    @app.route("/")
    def home():
        if htmx:
            return render_template("partials/thing.html")
        return render_template("index.html")

The above example checks whether the request came
from HTMX or not. If :code:`htmx` evaluates to
:py:obj:`True`, then it was a HTMX request, else
:py:obj:`False`.

This allows you to return a partial
HTML when it's a HTMX request or the full page HTML
when it is a normal browser request.

Flask-HTMX also supports checking for HTMX headers
during a request in the view. For example, check
the current URL of the browser of a HTMX request.

.. code-block:: python

    @app.route("/")
    def home():
        current_url = htmx.current_url
        return render_template("index.html", current_url=current_url)

Other HTMX request headers are also available.
See https://htmx.org/reference/#request_headers.