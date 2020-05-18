import json


def convert_dict(data):
    try:
        if type(data) is bytes:
            return json.loads(data.decode('utf-8'))
        elif type(data) is str:
            return json.loads(data)
        else:
            return data

    except Exception as ex:
        return data

