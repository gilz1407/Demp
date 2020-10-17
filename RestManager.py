import requests

from Interfaces.IStrategy import IStrategy


class RestManager:
    def __init__(self):
        pass

    def post_request(self, strategy: IStrategy):
        res = requests.get("https://petstore.swagger.io/v2/pet/findByStatus", params={"status":"ssold"})
        print(res)

    def get_request(self, strategy: IStrategy):
        pass

    def update_request(self, strategy: IStrategy):
        pass

    def delete_request(self, strategy: IStrategy):
        pass

rest = RestManager()
rest.post_request(None)
