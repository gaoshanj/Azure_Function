
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    # 从 query string 获取 name 参数
    name = req.params.get('name')

    # 如果 query 没有，则尝试从 JSON body 获取
    if not name:
        try:
            req_body = req.get_json()
            name = req_body.get('name')
        except ValueError:
            pass

    # 返回结果
    if name:
        return func.HttpResponse(f"Hello, {name}!", status_code=200)
    else:
        return func.HttpResponse(
            "Please provide a name in query string or request body.",
            status_code=400
        )
