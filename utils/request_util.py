import requests


class RequestUtil:
    # 全局会话，保持cookie
    session = requests.Session()

    @classmethod
    def send_all_request(cls, **kwargs):
        # 1. 取出 token
        token = kwargs.pop("token", None)

        # 2. 如果有token，自动塞进 headers
        if token:
            headers = kwargs.get("headers", {})
            headers["Authorization"] = token
            kwargs["headers"] = headers

        # 3. 发送原生请求
        res = cls.session.request(**kwargs)
        return res