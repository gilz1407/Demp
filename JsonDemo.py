from resDemo import res

class demo:
    def __init__(self, destination_addresses=None, text=None):
        self.rows_elements_distance_text = destination_addresses
        self.text = text



def json_extract(obj, key,object = None, set=False ):
    arr = []

    def extract(obj, arr, key):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    if key.__contains__(k):
                        if len(key) > 2:
                            key.pop()
                            print(key)
                        if set is True:
                            lst = vars(object).items()
                            for item,value in lst:
                                if item == k:
                                    setattr(object, k, value)
                            return True
                        #if len(key) == 1:
                        #    return v
                    extract(v, arr, key)
                elif key.__contains__(k) and key[]:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values



def json_extract_old(obj, key,object = None, set=False ):
    arr = []

    def extract(obj, arr, key):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    if k == key:
                        if set is True:
                            lst = vars(object).items()
                            for item,value in lst:
                                if item == k:
                                    setattr(object, k, value)
                            return True
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
        if item.__contains__("_"):
            lst = item.split("_")[::-1]
            travel_values = json_extract(res, lst)
        if len(travel_values) > 0:
            setattr(obj, item, travel_values)
    return obj

def init_req(obj):
    lst = vars(obj).items()
    for item, value in lst:
        travel_values = json_extract(res, item, obj, True)
        if len(travel_values) > 0:
            setattr(obj, item, travel_values)
    return obj

d = demo()
res = init_obj(d)
print(res)

#d1 = demo(destination_addresses=["TA, ISRAEL", "Haifa, PA, ISRAEL"])
#init_req(d1)