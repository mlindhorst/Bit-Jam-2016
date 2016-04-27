import json
SAVE_FILE = "save.json"

def save( door, person ):
    #save game state
    save_state = json.dumps({"door": door, "person": person})
    file = open(SAVE_FILE, 'w')
    file.write(save_state)
    file.close()