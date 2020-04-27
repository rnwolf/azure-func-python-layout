"""Shared functions that we can use in our Azure Fuctions can go here."""


def hello():
    """Say Hello, so that we can check shared code."""
    return b"hello"


def get_name(req):
    """Get the name passed to trigger via url or body."""
    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
        except AttributeError:
            name = None
        else:
            name = req_body.get("name")
    return name
