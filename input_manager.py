import Saver

class Inputer(object):

    def __init__(self, root, looper):
        self.root = root
        self.looper = looper
        self.done = 0
        self.root.bind("<Key>", self.key_pressed)
        self.current_input  = ""
        self.current_callsign  = ""
        self.changingNPC = False

    def key_pressed(self, event):
        print("pressed", repr(event.char))
        if(event.char == '\r'):
            if(self.changingNPC):         
                self.root.event_generate("<<ChangeNPC>>")
                self.current_callsign = ""
                self.changingNPC = False
                return
            else:
                self.root.event_generate("<<InputEntered>>")
                self.current_input = ""
                return
        # Backspace = delete
        if(event.char == '\x08'):
            self.current_input = ""
            return
        # Save Command - ctrl+s
        if(event.char == '\x13'):
            Saver.save(self.looper.current_door, self.looper.current_character)
            self.current_input = ""
            return
        # Exit Command - esc
        if(event.char == '\x1b'):
            self.root.destroy()
            self.current_input = ""
            return
        # Repeat Last Message Command - ctrl+r
        if(event.char == '\x12'):
            self.root.event_generate("<<Replay>>")
            self.current_input = ""
            return
        # Change NPCs Command - ctrl+c + callsign
        if(event.char == '\x03'):
            self.changingNPC = True
            self.current_input = ""
            return
        
        if(self.changingNPC):
            self.current_callsign += event.char
        else:                
            self.current_input += event.char
            print(self.current_input)
  