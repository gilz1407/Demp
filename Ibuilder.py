import json
from abc import ABC

from Rest import Rest


class Ibuilder(ABC):

    def __init__(self, value):
        self.value = value
        self.rest = Rest()
        super().__init__()

    def read_request_template(self, request_name):
        with open('requests.json') as request_file:
            data = json.load(request_file)
            requests_lst = data["requests"]
            for request in requests_lst:
                if request["name"] == request_name:
                    return request["query"]
