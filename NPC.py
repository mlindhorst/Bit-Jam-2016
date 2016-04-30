import Loader

class NPC:    
    def __init__(self, name, door_num, responses):
        self.name = name
        self.door_num = door_num
        self.responses = responses
        
    def get_response(self, question_number):
        return self.responses[question_number]
        
class NPCCreator:
    def __init__(self):
        print ('NPCs created.')
        
    def create_all(self):
        return Loader.load_npcs()