"""An example Azure Function triggered by an HTTP get or post."""
import logging
import azure.functions as func
from __app__.sharedcode import my_helper_functions


def main(req: func.HttpRequest) -> func.HttpResponse:
    """Deal with HttpTrigger1 event."""
    logging.info("Python HTTP trigger function processed a request.")
    logging.info(
        "Run shared code function %s ", my_helper_functions.hello()
    )  # pylint: disable=I0011,E1205

    name = my_helper_functions.get_name(req)

    if name:
        return func.HttpResponse(f"Hello it is trigger2 here, {name}!")
    return func.HttpResponse(
        """Please pass a name on the query string
        or in the request body as a json unicode string.""",
        status_code=400,
    )
