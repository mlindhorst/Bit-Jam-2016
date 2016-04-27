from Loader import load_npcs

class NPC:    
    def __init__(self, name, responses):
        self.name = name
        self.responses = responses
        
    def get_response(self, question_number):
        return responses[question_number]
        
class NPCCreator:
    def __init__(self):
        print ('NPCs created.')
        
    def create_all(self):
        return load_npcs()