import json

def deserialize_json_from_file (filename):
    jsonFile = open(filename)
    return json.load(jsonFile)





print(deserialize_json_from_file("C:\\Users\\jason_kallman\\Documents\\GitHub\\Bit-Jam-2016\\test.json")["Pokemon"])
