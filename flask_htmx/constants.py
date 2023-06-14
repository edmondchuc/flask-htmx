#: True and False values for the HX-* request and response headers
HX_TRUE = "true"
HX_FALSE = "false"

#: Values allowed for the HX-Reswap response header
RESWAPS = [
    "innerHTML",
    "outerHTML",
    "beforebegin",
    "afterbegin",
    "beforeend",
    "afterend",
    "delete",
    "none",
]

#: If you want to stop polling from a server response you can respond with the HTTP
#: response code 286 and the element will cancel the polling.
HTMX_STOP_POLLING = 286
