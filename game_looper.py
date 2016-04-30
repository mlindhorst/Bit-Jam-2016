import Translator
import blinker
import Door
import input_manager

class Looper(object):
    
    def __init__(self, root):
        self.root = root
        self.done = 0 
        self.inputer = input_manager.Inputer(root, self)  
        
    def intro(self):
        print("Level 0")
        sos = Translator.translate_to_morse_code("SOS")
        self.current_level = 1
        self.root.bind("<<FlashingDone>>", self.begin_loop)
        self.game_blinker.flash(sos)
        
    def start(self, door):
        self.game_blinker = blinker.Blinker(self.root)
        self.intro()
        
    def load(self, door_num):
        self.game_blinker = blinker.Blinker(self.root)
        self.current_level = door_num
        self.begin_loop()
   
    def begin_loop(self, *args):
        self.root.unbind("<<FlashingDone>>")   

        doorCreator = Door.DoorCreator()
        self.current_door = doorCreator.get_door(str(self.current_level))
        self.current_character = self.current_door.npcs[0]
             
        self.root.bind("<<InputEntered>>", self.parse_answer)
             
        
    def parse_answer(self, *args):
        user_input = self.inputer.current_input
        self.root.unbind("<<InputEntered>>")        
        input_length = len(user_input)
        
        #question # is entered
        if(input_length == 1):
            response = self.current_character.get_response(user_input)[0]
            response_morse = Translator.translate_to_morse_code(response)
            self.root.bind("<<FlashingDone>>", self.begin_loop)
            self.game_blinker.flash(response_morse)
            
        if(input_length == 4):
            input_list = list(user_input)
            current_key = list(self.current_door.key)
  
            
            
            
  
    
    