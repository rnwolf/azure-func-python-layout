"""Test the http_trigger_1 Azure function."""
# tests/test_http_trigger_1.py

from hypothesis import given, example
from hypothesis.strategies import text
import azure.functions as func
from __app__.http_trigger_1 import main


@given(input_text=text())
@example(input_text="")
def test_func_for_user_names_via_params(input_text):
    """Construct a mock HTTP request."""
    req = func.HttpRequest(
        method="POST", body=None, url="/api/http_trigger_1", params={"name": input_text}
    )

    # Call the function.
    resp = main(req)

    # Check the output.
    if input_text:
        assert (  # nosec(
            resp.get_body() == b"Hello from trigger 1, " + str.encode(input_text) + b"!"
        )
    else:
        assert (  # nosec
            resp.get_body()
            == b"Please pass a name on the query string or in the request body"
        )


# @given(input_text=text())
# @example(input_text='')
def test_func_for_user_names_via_body(input_text="Test"):
    """Construct a mock HTTP request."""
    req = func.HttpRequest(
        method="POST",
        body=b'{"name":"' + str.encode(input_text) + b'"}',
        url="/api/http_trigger_1",
        params={},
    )

    # Call the function.
    resp = main(req)

    # Check the output.
    if input_text:
        assert (  # nosec
            resp.get_body() == b"Hello from trigger 1, " + str.encode(input_text) + b"!"
        )
    else:
        assert (  # nosec
            resp.get_body()
            == b"Please pass a name on the query string or in the request body"
        )


def test_func_for_no_name():
    """Construct a mock HTTP request."""
    req = func.HttpRequest(
        method="POST", body=None, url="/api/http_trigger_1", params={}
    )

    # Call the function.
    resp = main(req)

    # Check the output.
    assert (  # nosec
        resp.get_body()
        == b"Please pass a name on the query string or in the request body"
    )
