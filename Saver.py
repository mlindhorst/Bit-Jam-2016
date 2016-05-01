import json
SAVE_FILE = "save.json"

def save( door, person ):
    #bad things, don't look at this!
    if(door.name == 'Communications'):        
        save_state = json.dumps({"door": 1, "person": person.name})
    elif(door.name == 'Armory'):        
        save_state = json.dumps({"door": 2, "person": person.name})
    elif(door.name == 'Entry'):        
        save_state = json.dumps({"door": 3, "person": person.name})
    
    #save game state
    file = open(SAVE_FILE, 'w')
    file.write(save_state)
    file.close()