#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An example Azure Function triggered by an HTTP get or post."""
# __app__\http_trigger_2\__init__.py
import logging
import azure.functions as func
from __app__.sharedcode import my_helper_functions


def main(req: func.HttpRequest) -> func.HttpResponse:
    """Deal with http_trigger_2 event."""
    logging.info("Python HTTP trigger function processed a request.")
    logging.info(
        "Run shared code function %s ", my_helper_functions.hello()
    )  # pylint: disable=I0011,E1205

    name = my_helper_functions.get_name(req)

    if name:
        return func.HttpResponse(f"Hello from trigger 1, {name}!")
    return func.HttpResponse(
        "Please pass a name on the query string or in the request body",
        status_code=400,
    )
