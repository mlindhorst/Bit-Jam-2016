import NPC

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

    def __init__(self):
        self.npcs_list = NPC.NPCCreator().create_all()
        self.create_doors()
        
    def create_doors(self):    
        for npc in self.npcs_list:
            self.doors[npc.door_num].npcs.append(npc)
            if int(npc.door_num) < 3:
                self.doors[3].npcs.append(npc)
            if int(npc.door_num) < 2:
                self.doors[2].npcs.append(npc)
        
    def get_door(self, door_num):
        return self.doors[door_num]
