
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
            json.dumps({"error": "Missing 'prompt' in request body."}, ensure_ascii=False),
            status_code=400,
            mimetype="application/json"
        )

    endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
    key = os.environ.get("AZURE_OPENAI_KEY")
    deployment = os.environ.get("OPENAI_DEPLOYMENT_NAME") or "gpt-5-nano"  # 请替换为你的部署名

    if not endpoint or not key:
        return func.HttpResponse(
            json.dumps({
                "error": "Azure OpenAI credentials not configured. Please set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_KEY."
            }, ensure_ascii=False),
            status_code=500,
            mimetype="application/json"
        )

    try:
        client = OpenAIClient(endpoint=endpoint, credential=AzureKeyCredential(key))

        # 组装消息
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        # 正确的调用方法
        response = client.get_chat_completions(
            deployment_id=deployment,
            messages=messages
        )

        # 解析返回
        content = None
        try:
            if response.choices and response.choices[0].message:
                content = response.choices[0].message.content
        except Exception:
            content = None

        if content is None:
            content = ""

        return func.HttpResponse(
            json.dumps({"reply": content}, ensure_ascii=False),
            status_code=200,
            mimetype="application/json"
        )
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": "OpenAI request failed.", "diagnostic": str(e)}, ensure_ascii=False),
            status_code=500,
            mimetype="application/json"
        )
