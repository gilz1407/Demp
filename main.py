from Builder import Builder
from DataModel import GenericQuery

builder = Builder()
gq = GenericQuery()
gq.user_name = "gil_zur"
gq.user_age = 36
gq.user_id = 123
builder.generic_query_builder(gq)