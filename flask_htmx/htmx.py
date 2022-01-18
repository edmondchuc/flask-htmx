from typing import Optional

from flask import Flask, request


class HTMX:
    """
    Flask-HTMX is a Flask extension which provides an easy API to work
    with HTMX from within a Flask request context.

    Inspired by the Django extension Django-HTMX.

    See also:

    - https://htmx.org/reference/#request_headers
    - https://github.com/adamchainz/django-htmx
    """

    def __init__(self, app: Flask = None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        """Initialise the extension with the Flask app object."""
        app.htmx = self

    @property
    def boosted(self) -> bool:
        """:py:obj:`True` if the request came from an element with the `hx-boost` attribute.

        Based on the :code:`HX-Boosted` header.
        """
        return request.headers.get("HX-Boost") == "true"

    @property
    def current_url(self) -> Optional[str]:
        """The current URL of the browser, or :py:obj:`None` for non-HTMX requests.

        Based on the :code:`HX-Current-URL` header.
        """
        return request.headers.get("HX-Current-URL")

    @property
    def history_restore_request(self) -> bool:
        """:py:obj:`True` if the request is for history restoration after a miss in the local history cache.

        Based on the :code:`HX-History-Restore-Request` header.
        """
        return request.headers.get("HX-History-Restore-Request") == "true"

    @property
    def prompt(self) -> Optional[str]:
        """The user response to :code:`hx-prompt` if it was used, or :py:obj:`None`."""
        return request.headers.get("HX-Prompt")

    def __bool__(self) -> bool:
        """:py:obj:`True` if the request was made with HTMX, otherwise :py:obj:`False`.

        This is based on the presence of the :code:`HX-Request` header.
        """
        return request.headers.get("HX-Request") == "true"

    @property
    def target(self) -> Optional[str]:
        """The ID of the target element if it exists, or :py:obj:`None`.

        Based on the :code:`HX-Target header`.
        """
        return request.headers.get("HX-Target")

    @property
    def trigger_name(self) -> Optional[str]:
        """The name of the triggered element if it exists, or :py:obj:`None`.

        Based on the :code:`HX-Trigger-Name` header.
        """
        return request.headers.get("HX-Trigger-Name")

    @property
    def trigger(self) -> Optional[str]:
        """The ID of the triggered element if it exists, or :py:obj:`None`.

        Based on the :code:`HX-Trigger` header.
        """
        return request.headers.get("HX-Trigger")
