import json
from abc import ABC, abstractmethod

class IStrategy(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def build_post_request(self):
        pass

    @abstractmethod
    def build_update_request(self):
        pass

    def read_request_template(self, request_name):
        with open("Services/PetStore/requests.json") as request_file:
            data = json.load(request_file)
            requests_lst = data["requests"]
            for request in requests_lst:
                if request["request_name"] == request_name:
                    return request