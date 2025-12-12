import os
import json
import azure.functions as func
from azure.ai.openai import OpenAIClient
from azure.core.credentials import AzureKeyCredential


def main(req: func.HttpRequest) -> func.HttpResponse:
    # Parse request body
    try:
        req_body = req.get_json()
    except ValueError:
        req_body = None

    prompt = None
    system_prompt = None
    if req_body:
        prompt = req_body.get("prompt")
        system_prompt = req_body.get("systemPrompt") or req_body.get("system_prompt")

    if not prompt:
        return func.HttpResponse(
            json.dumps({"error": "Missing 'prompt' in request body."}),
            status_code=400,
            mimetype="application/json"
        )

    endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
    key = os.environ.get("AZURE_OPENAI_KEY")
    deployment = os.environ.get("OPENAI_DEPLOYMENT_NAME") or "gpt-5-nano"

    if not endpoint or not key:
        return func.HttpResponse(
            json.dumps({"error": "Azure OpenAI credentials not configured (AZURE_OPENAI_ENDPOINT / AZURE_OPENAI_KEY)."}),
            status_code=500,
            mimetype="application/json"
        )

    try:
        client = OpenAIClient(endpoint, AzureKeyCredential(key))
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = client.chat_completion(deployment_id=deployment, messages=messages)
        content = None
        try:
            content = response.choices[0].message.content
        except Exception:
            content = getattr(response, "content", None)

        if content is None:
            content = ""

        return func.HttpResponse(
            json.dumps({"reply": content}),
            status_code=200,
            mimetype="application/json"
        )
    except Exception as e:
        diag = str(e)
        return func.HttpResponse(
            json.dumps({"error": "OpenAI request failed.", "diagnostic": diag}),
            status_code=500,
            mimetype="application/json"
        )
