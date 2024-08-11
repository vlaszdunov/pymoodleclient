from .endpoints.base import Endpoint, ResponseObject
from .request_params import Params
from dataclasses import asdict


class Client:
    url: str
    token: str

    def __init__(self, url: str, token: str):
        self.url = url
        self.token = token

    def call(self, endpoint: Endpoint) -> ResponseObject:
        response: ResponseObject = endpoint.response_object(
            endpoint.request_type(
                f"{self.url}/webservice/rest/server.php",
                params=asdict(Params(self.token, endpoint.function_name)),
            ).json()
        )
        return response
