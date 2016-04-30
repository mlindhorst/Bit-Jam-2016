import Saver

class Inputer(object):

    def __init__(self, root, looper):
        self.root = root
        self.looper = looper
        self.done = 0
        self.root.bind("<Key>", self.key_pressed)
        self.current_input  = ""

    def key_pressed(self, event):
        print("pressed", repr(event.char))
        if(event.char == '\r'):
             self.root.event_generate("<<InputEntered>>")
             self.current_input = ""
             return
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
            print("repeat!")
            self.current_input = ""
            return
        # Change NPCs Command - ctrl+c + callsign???
        if(event.char == '\x03'):
            print("change npcs!")
            self.current_input = ""
            return
        self.current_input += event.char
        print(self.current_input)
  