import logging
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger for CI/CD TestCI processed a request.")
    return func.HttpResponse("CI/CD test successful", status_code=200)
