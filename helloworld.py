from tkinter import *

#root = ordinary window with title bar
root = Tk()

#Label = display either text or an icon or other image
w = Label(root, text="Hello, world!")
#pack = tells widget to size itself to fit the given text,
#and make itself visible
w.pack()

#make window appear
root.mainloop()