import Translator
import blinker
import Door
import input_manager
import copy

class Looper(object):
    
    def __init__(self, root):
        self.root = root
        self.done = 0 
        self.inputer = input_manager.Inputer(root, self)  
        self.game_blinker = blinker.Blinker(self.root)
        self.current_character = None    
        self.current_message = {}        
        
        
    def start(self, door):
        self.current_level = 1
        self.current_NPC = 0            
        self.intro()
        
    def intro(self):
        print("Level 0")
        self.current_message = "SOS"        
        self.play_message()
        
    def load(self, door_num):
        #self.game_blinker = blinker.Blinker(self.root)
        self.current_level = door_num
        self.begin_loop()        
   
    def begin_loop(self, *args):
        print("begining loop")
        self.root.unbind("<<FlashingDone>>") 
        
        doorCreator = Door.DoorCreator()
        self.current_door = doorCreator.get_door(self.current_level)
        #if(self.current_character == None):   
        self.current_character = self.current_door.npcs[0]      
            
        self.root.bind("<<InputEntered>>", self.parse_answer)
        self.root.bind("<<ChangeNPC>>", self.parse_change)
        self.root.bind("<<Replay>>", self.play_message)  
    
    def parse_change(self, *args):        
        call_sign = self.inputer.current_callsign
        for n in self.current_door.npcs:
            if n.name == call_sign:
                current_character = n             
                begin_loop()
                return             
        
    def parse_answer(self, *args):
        user_input = self.inputer.current_input
        print("Parsing answer: " + user_input)               
        input_length = len(user_input)
        
        if(input_length == 1 or input_length == 4):
            if(input_length == 1):
                # should get_response take in door # to determine response
                response = self.current_character.get_response(user_input)
                if(response is None):
                    print("Unable to find response for: " + user_input)
                    self.begin_loop()
                    return
                else:
                    self.current_message = response[0]
                    self.play_message()
            if(input_length == 4):
                input_list = list(user_input)
                current_key = list(self.current_door.key)
                input_list.sort()
                current_key.sort()
                
                sorted_input = "".join(input_list)
                sorted_key = "".join(current_key)
                
                if(sorted_input == sorted_key):
                    self.current_level+=1
                    print(self.current_level)
                    #this should be transmitting good text, and then start of next door
                    self.begin_loop()
          
    def play_message(self, *args):
        print("playing: " + self.current_message)
        self.root.unbind("<<InputEntered>>")
        self.root.unbind("<<ChangeNPC>>")
        self.root.unbind("<<Replay>>")  
        self.root.bind("<<FlashingDone>>", self.begin_loop)
        self.game_blinker.flash(copy.copy(Translator.translate_to_morse_code(self.current_message)))      