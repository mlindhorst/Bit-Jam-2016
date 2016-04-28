import Translator
import blinker

class Looper(object):
    
    def __init__(self, root):
        self.root = root
        
    def intro(self):
        sos = Translator.translate_to_morse_code("SOS")
        self.game_blinker.flash(sos)
        
    def start(self):
        self.game_blinker = blinker.Blinker(self.root)
        self.intro()

    