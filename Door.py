class Door:
    def __init__(self, name, key, npcs):
        self.name = name
        self.key = key
        self.npcs = npcs
        
class DoorCreator:
    doors = {
        1 : Door('Communications', '1984', []),
        2 : Door('Armory', '5712', []),
        3 : Door('Entry', '9011', [])
    }

    def __init__(self, npcs_list):
        self.npcs_list = npcs_list
        self.create_doors()
        
    def create_doors(self):    
        for npc in self.npcs_list:
            self.doors[npc.door_num].npcs.append(npc)
        
    def get_door(self, door_num):
        return self.doors[door_num]
