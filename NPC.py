import Loader

class NPC:    
    def __init__(self, name, door_num, responses):
        self.name = name
        self.door_num = door_num
        self.responses = responses
        
    def get_response(self, question):
        if(question.isdigit()):
            question_number = int(question)
            if(question_number > 0 and question_number < 7):
                return self.responses[question]
            else:
                return None
        else:
            return None
        
class NPCCreator:
    def __init__(self):
        print ('NPCs created.')
        
    def create_all(self):
        return Loader.load_npcs()