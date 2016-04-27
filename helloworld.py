from tkinter import *

#root = ordinary window with title bar
root = Tk()

#Label = display either text or an icon or other image
w = Label(root, text="Hello, world!")
#pack = tells widget to size itself to fit the given text,
#and make itself visible
w.pack()

#make window appear
#The program will stay in the event loop until we close the window. 
#The event loop doesn’t only handle events from the user (such as 
#mouse clicks and key presses) or the windowing system (such as 
#redraw events and window configuration messages)
root.mainloop()