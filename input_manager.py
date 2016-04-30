class Inputer(object):

    def __init__(self, root):
        self.root = root
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
        self.current_input += event.char
        print(self.current_input)
  