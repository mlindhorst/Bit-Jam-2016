
from tkinter import *
import time
import winsound, sys

class Blinker(object):    
    
    global OFF_MSEC
    global DOT_MSEC
    global DASH_MSEC
    global LETTER_MSEC
    global WORD_MSEC
    global OFF
    global ON
        
    OFF_MSEC = 400
    DOT_MSEC = 500
    LETTER_MSEC = 600
    WORD_MSEC = 1500
    DASH_MSEC = 1500
    OFF = 'light blue'
    ON = 'maroon'
    
    def __init__(self, root):
        self.root = root

    def flash(self, signals): 
        current_background = self.root["background"]
        if not signals:
            self.root.configure(background = OFF)
            self.root.event_generate("<<FlashingDone>>")
            return;
        signal = signals.pop(0)        
        if(current_background == ON):
            self.root.configure(background = OFF)
            if(signal == '|'):
                self.root.after(LETTER_MSEC, self.flash, signals)
            elif(signal == '$'):
                self.root.after(WORD_MSEC, self.flash, signals)
            else:
                signals.insert(0, signal)
                self.root.after(OFF_MSEC, self.flash, signals)                
        elif (current_background == OFF):
            if(signal == '-'):
                self.dash(signals)
            elif(signal == '.'):
                self.dot(signals)
            elif(signal == '$'):
                self.root.after(WORD_MSEC, self.flash, signals) 
            elif(signal == '|'):
                self.root.after(LETTER_MSEC, self.flash, signals)      
                
    def dash(self, signals): 
        self.root.configure(background = ON)
        self.root.after(DASH_MSEC, self.flash, signals)
        winsound.PlaySound('beep-dash.wav', winsound.SND_FILENAME | winsound.SND_ASYNC )
        
    def dot(self, signals): 
        self.root.configure(background = ON)        
        self.root.after(DOT_MSEC, self.flash, signals)
        winsound.PlaySound('beep-dot.wav', winsound.SND_FILENAME | winsound.SND_ASYNC )