import Translator
import blinker
import Door
import input_manager

class Looper(object):
    
    def __init__(self, root):
        self.root = root
        self.done = 0 
        self.inputer = input_manager.Inputer(root, self)  
        self.game_blinker = blinker.Blinker(self.root)
        
    def intro(self):
        print("Level 0")
        sos = Translator.translate_to_morse_code("SOS")        
        self.root.bind("<<FlashingDone>>", self.begin_loop)
        self.game_blinker.flash(sos)
        
    def start(self, door):
        self.current_level = 1
        self.current_NPC = 0
        self.current_character = None        
        self.intro()
        
    def load(self, door_num):
        self.game_blinker = blinker.Blinker(self.root)
        self.current_level = door_num
        self.begin_loop()
   
    def begin_loop(self, *args):
        self.root.unbind("<<FlashingDone>>")   

        doorCreator = Door.DoorCreator()
        self.current_door = doorCreator.get_door(str(self.current_level))
        if(self.current_character == None):   
            self.current_character = self.current_door.npcs[0]
             
        self.root.bind("<<InputEntered>>", self.parse_answer)
        self.root.bind("<<ChangeNPC>>", self.parse_change)
    
    def parse_change(self, *args):        
        call_sign = self.inputer.current_callsign
        for n in self.current_door.npcs:
            if n.name == call_sign:
                current_character = n             
                begin_loop()
                return             
        
    def parse_answer(self, *args):
        user_input = self.inputer.current_input
        self.root.unbind("<<InputEntered>>")        
        input_length = len(user_input)
        
        #question # is entered
        if(input_length == 1):
            # should get_response take in door # to determine response
            response = self.current_character.get_response(user_input)[0]
            response_morse = Translator.translate_to_morse_code(response)
            self.root.bind("<<FlashingDone>>", self.begin_loop)
            self.game_blinker.flash(response_morse)
            
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
          
                
  
            
            
            
  
    
    