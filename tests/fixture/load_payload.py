import json

def load_json_payload(file_name):
    with open("tests/fixture/json_payload/{}.json".format(file_name)) as json_file:
        return json_file.read()

def load_json_as_dict(file_name):
    return json.loads(load_json_payload(file_name))