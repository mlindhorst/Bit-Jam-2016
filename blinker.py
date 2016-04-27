
from tkinter import *
import time
import winsound, sys

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
    
def flash(root, signals):    
    current_background = root["background"]
    if not signals:
        root.configure(background = OFF)
        return;
    signal = signals.pop(0)        
    if(current_background == ON):
        root.configure(background = OFF)
        if(signal == '|'):
            root.after(LETTER_MSEC, flash, root, signals)
        elif(signal == '&'):
            root.after(WORD_MSEC, flash, root, signals)
        else:
            signals.insert(0, signal)
            root.after(OFF_MSEC, flash, root, signals)                
    elif (current_background == OFF):
        if(signal == '-'):
            dash(root, signals)
        elif(signal == '.'):
            dot(root, signals)
            
def dash(root, signals): 
    root.configure(background = ON)
    root.after(DASH_MSEC, flash,root, signals)
    winsound.PlaySound('beep-dash.wav', winsound.SND_FILENAME | winsound.SND_ASYNC )
    
def dot(root, signals): 
    root.configure(background = ON)        
    root.after(DOT_MSEC, flash, root, signals)
    winsound.PlaySound('beep-dot.wav', winsound.SND_FILENAME | winsound.SND_ASYNC )