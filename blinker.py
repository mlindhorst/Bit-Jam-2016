
from tkinter import *
import pygame

class App:

    def __init__(self, master):    
        frame = Frame(master)
        frame.pack()       
        
        self.hi_there = Button(frame, text="Hello", command=self.dash)
        self.hi_there.pack(side=LEFT)
        
    def dot(self):
        print("dot")
        root.configure(background='maroon')
        root.after(250, self.off)     
   
    def dash(self):
        print("dash")
        root.configure(background='maroon')
        root.after(750, self.off) 
        root.update_idletasks()
        return "true"       
    
    def off(self):
        print("off")
        root.configure(background="light blue")
                

root = Tk()

root.configure(background='light blue')
root.minsize(width=1024, height=600)

app = App(root)
app.dot()
app.dash()
root.mainloop()