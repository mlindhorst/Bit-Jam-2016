import json
from JsonFileReader import *
from SaveState import *

def load_save_state():
    save_file_json = deserialize_json_from_file("save.json")
    return SaveState(save_file_json["door"], save_file_json["person"])