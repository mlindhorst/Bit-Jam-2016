import json
from JsonFileReader import *
from SaveState import *
import NPC

def load_save_state():
    save_file_json = deserialize_json_from_file("save.json")
    return SaveState(save_file_json["door"], save_file_json["person"])
            
def load_npcs():    
    npcs = []
    save_file_json = deserialize_json_from_file('npcs.json')
    for json_npc in save_file_json:
        character = NPC.NPC(json_npc['name'], json_npc['responses'])
        npcs.append(character)
    return npcs