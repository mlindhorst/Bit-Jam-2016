
from tkinter import *
import time

class App:    
    
    global OFF_MSEC
    global DOT_MSEC
    global DASH_MSEC
    global LETTER_MSEC
    global WORD_MSEC
    global OFF
    global ON
        
    OFF_MSEC = 400
    DOT_MSEC = 500
    LETTER_MSEC = 750
    WORD_MSEC = 1500
    DASH_MSEC = 1500
    OFF = 'light blue'
    ON = 'maroon'
        
    def flash(self, signals):    
        current_background = root["background"]
        if not signals:
            root.configure(background = OFF)
            return;
        signal = signals.pop(0)        
        if(current_background == ON):
            root.configure(background = OFF)
            if(signal == '|'):
                root.after(LETTER_MSEC, self.flash, signals)
            elif(signal == '&'):
                root.after(WORD_MSEC, self.flash, signals)
            else:
                signals.insert(0, signal)
                root.after(OFF_MSEC, self.flash, signals)                
        elif (current_background == OFF):
            if(signal == '-'):
                self.dash(signals)
            elif(signal == '.'):
                self.dot(signals)
                
    def dash(self, signals): 
        root.configure(background = ON)
        root.after(DASH_MSEC, self.flash, signals)
        
    def dot(self, signals): 
        root.configure(background = ON)
        root.after(DOT_MSEC, self.flash, signals)
        
root = Tk()

root.configure(background='light blue')
root.minsize(width=1024, height=600)

app = App()
AB = ['.', '-', '|', '-', '.', '.', '.']
root.after(400, app.flash, AB)
root.mainloop()