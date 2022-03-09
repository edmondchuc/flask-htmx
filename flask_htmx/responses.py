from flask import Response


#: If you want to stop polling from a server response you can respond with the HTTP response code 286 and
#: the element will cancel the polling.
HTMX_STOP_POLLING = 286


class HTMXResponseClientRedirect(Response):
    """Flask response to instruct HTMX to perform a client-side redirect."""

    def __init__(self, redirect_to: str, status: int = 200):
        super(HTMXResponseClientRedirect, self).__init__(
            None, status=status, headers={"HX-Redirect": redirect_to}
        )


class HTMXResponseStopPolling(Response):
    """Flask response to instruct HTMX to stop polling."""

    def __init__(
        self,
        response=None,
        headers=None,
        mimetype="text/html",
        direct_passthrough=False,
    ):
        super(HTMXResponseStopPolling, self).__init__(
            response=response,
            status=HTMX_STOP_POLLING,
            headers=headers,
            mimetype=mimetype,
            direct_passthrough=direct_passthrough,
        )
