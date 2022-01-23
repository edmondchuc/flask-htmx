##########
Flask-HTMX
##########

.. image:: https://badge.fury.io/py/flask-htmx.svg
    :target: https://badge.fury.io/py/flask-htmx

.. image:: https://readthedocs.org/projects/flask-htmx/badge/?version=latest
    :target: https://flask-htmx.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


.. image:: https://codecov.io/gh/edmondchuc/flask-htmx/branch/main/graph/badge.svg?token=K6YB3PB33T
    :target: https://codecov.io/gh/edmondchuc/flask-htmx


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/License-MIT-red.svg
    :target: https://github.com/edmondchuc/flask-htmx/blob/main/LICENSE

.. image:: https://static.pepy.tech/personalized-badge/flask-htmx?period=month&units=international_system&left_color=grey&right_color=blue&left_text=downloads/week
    :target: https://pepy.tech/project/flask-htmx

.. image:: https://static.pepy.tech/personalized-badge/flask-htmx?period=month&units=international_system&left_color=grey&right_color=blue&left_text=downloads/month
    :target: https://pepy.tech/project/flask-htmx

.. image:: https://static.pepy.tech/personalized-badge/flask-htmx?period=total&units=international_system&left_color=grey&right_color=blue&left_text=downloads
    :target: https://pepy.tech/project/flask-htmx

A Flask extension to work with HTMX.

Documentation: https://flask-htmx.readthedocs.io

.. quickstart-startblock

Quickstart
==========

Install the extension with pip.

.. code-block:: bash

    pip install flask-htmx

Or perhaps you use Poetry.

.. code-block:: bash

    poetry add flask-htmx

You can register the HTMX object by passing the Flask
:code:`app` object via the constructor.

.. code-block:: python

    htmx = HTMX(app)

Or you can register the HTMX object using
`HTMX.init_app() <https://flask-htmx.readthedocs.io/en/latest/flask_htmx.htmx.html#flask_htmx.htmx.HTMX.init_app>`_.

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
`True <https://docs.python.org/3/library/constants.html#True>`_, then it was a HTMX request, else
`False <https://docs.python.org/3/library/constants.html#False>`_.

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

Continue to the next section of the docs,
`The HTMX Class <https://flask-htmx.readthedocs.io/en/latest/flask_htmx.htmx.html>`_.

.. quickstart-endblock

Development
===========

Installation
------------

.. code-block:: bash

    poetry install

Running tests
-------------

.. code-block:: bash

    poetry run pytest

Coverage
--------

.. code-block:: bash

    poetry run pytest --cov=flask_htmx tests/

Docs
----

.. code-block:: bash

    sphinx-autobuild docs docs/_build/html
