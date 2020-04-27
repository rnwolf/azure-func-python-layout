#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test the http_trigger_2 Azure function."""
# tests/test_http_trigger_2.py

import azure.functions as func
from __app__.http_trigger_2 import main


TRIGGER_URL = "/api/http_trigger_2"


def test_func_for_user_names_via_params():
    """Construct a mock HTTP request."""
    req = func.HttpRequest(
        method="POST", body=None, url=TRIGGER_URL, params={"name": "Test"}
    )

    # Call the function.
    resp = main(req)

    # Check the output.
    assert resp.get_body() == b"Hello it is trigger2 here, Test!"  # nosec


def test_func_for_user_names_via_body():
    """Construct a mock HTTP request."""
    req = func.HttpRequest(
        method="POST", body=b'{"name":"Test"}', url=TRIGGER_URL, params={}
    )

    # Call the function.
    resp = main(req)

    # Check the output.
    assert resp.get_body() == b"Hello it is trigger2 here, Test!"  # nosec


def test_func_for_no_name():
    """Construct a mock HTTP request."""
    req = func.HttpRequest(method="POST", body=None, url=TRIGGER_URL, params={})

    # Call the function.
    resp = main(req)

    # Check the output.
    assert (  # nosec
        resp.get_body()
        == b"""Please pass a name on the query string
        or in the request body as a json unicode string."""
    )
