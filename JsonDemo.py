from resDemo import res

class demo:
    def __init__(self):
        self.destination_addresses = []
        self.text = []


def json_extract(obj, key):
    arr = []

    def extract(obj, arr, key):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    if k == key:
                        return v
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values

def init_obj(obj):
    lst = vars(obj).items()
    for item, value in lst:
        travel_values = json_extract(res, item)
        if len(travel_values) > 0:
            setattr(obj, item, travel_values)
    return obj


d = demo()
res = init_obj(d)
print(res)