from abc import ABC

from Interfaces.IStrategy import IStrategy


class PetDynamic:
    def __init__(self, pet_id, name, category_id, category_name):
        self.id = pet_id
        self.name = name
        self.category_id = category_id
        self.category_name = category_name


class PetStrategies(IStrategy, ABC):
    def __init__(self, value):
        super().__init__(value)
        self.curr_strategy = None
        self.api = "pet"
        self.request_template = super().read_request_template(self.api)
        self._req_data = {}

    def get_request_data(self):
        return self.request_template

    def get_request_template(self):
        return self._req_data

    def build_post_request(self):
        return {"/" + self.api, self.curr_strategy}

    def build_update_request(self):
        return {"/" + self.api, self.curr_strategy}

    def set(self, pet_id, category_id, category_name, name):
        self.request_template["id"] = pet_id
        self.request_template["category"]["id"] = category_id
        self.request_template["category"]["name"] = category_name
        self.request_template["name"] = name

        self._req_data["id"] = pet_id
        self._req_data["name"] = name
        self._req_data["category_id"] = category_id
        self._req_data["category_name"] = category_name

        self.curr_strategy = self.request_template

    def dynamic(self, pd: PetDynamic):
        self.set(pd.id, pd.category_id, pd.category_name, pd.name)

    def wrong_type_of_id(self, pd: PetDynamic):
        self.set("***", pd.category_id, "Cats", "Lilo")

    def mss(self):
        self.set(1234, 1234, "Cats", "Lilo")

    def random_mss(self):
        self.request_template["id"] = 1234
        self.request_template["category"]["id"] = 1234
        self.request_template["category"]["name"] = "Cats"
        self.request_template["name"] = "Lulu"
        return self.request_template
