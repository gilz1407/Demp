from DataModel import GenericQuery


def rest_type_one(builder):
    gq = GenericQuery(123)
    gq.user_name = "gil_zur"
    gq.user_age = 36
    return gq