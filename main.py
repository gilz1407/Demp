from Builder import Builder
from QueryObjects import rest_type_one

builder = Builder()
gq = rest_type_one(builder)
builder.generic_query_builder(gq)
