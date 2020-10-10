from Ibuilder import Ibuilder


class Builder(Ibuilder):
    def __init__(self, value=None):
        super().__init__(value)

    def generic_query_builder(self, generic_query):
        request_template = super().read_request_template(generic_query.__class__.__name__)
        request_template["userName"] = generic_query.user_name
        request_template["userId"] = generic_query.user_id
        request_template["userAge"] = generic_query.user_age
        response = self.rest.post(request_template)