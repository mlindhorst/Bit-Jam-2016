import json
SAVE_FILE = "save.json"

def save( door_num, person ):      
    save_state = json.dumps({"door": door_num, "person": person.name})
    file = open(SAVE_FILE, 'w')
    file.write(save_state)
    file.close()