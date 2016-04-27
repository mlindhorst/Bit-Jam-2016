import json

def deserialize_json_from_file (filename):
    jsonFile = open(filename)
    return json.load(jsonFile)