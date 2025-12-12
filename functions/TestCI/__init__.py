import logging
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        logging.info("TestCI Python function invoked. Processing request.")
        # Optional: inspect the request for debugging if needed
        # logging.debug(f"Request method={req.method}, url={req.url}, params={req.params}")
        return func.HttpResponse("CI/CD test successful", status_code=200)
    except Exception as e:
        logging.exception("Unhandled exception in TestCI function")
        error_body = {"error": "Internal server error", "detail": str(e)}
        return func.HttpResponse(
            json.dumps(error_body),
            status_code=500,
            headers={"Content-Type": "application/json"}
        )
