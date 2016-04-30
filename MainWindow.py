from tkinter import *
import blinker
import Loader
import game_looper

root = Tk()
root.configure(background='light blue')
root.minsize(width=1024, height=600)

menu_frame = Frame(root, width=800, height=400)
menu_frame.pack()
credits_frame = Frame(root, width=800, height=400)

def back_to_menu():
    credits_frame.pack_forget()
    menu_frame.pack()
    
def hide_menu():
    menu_frame.pack_forget() 

def new_game():
    hide_menu()
    looper = game_looper.Looper(root)    
    looper.start(0)

def load_game():
    hide_menu()
    current_load = Loader.load_save_state
    
def show_credits():
    hide_menu()
    credits_frame.pack()

#credits
programmers_title = Label(credits_frame, text="Programmers: Melynda Lindhorst, Sarah Ripley, Jason Kallman, Jonathan Meyer")
programmers_title.pack(side=TOP)
writer_title = Label(credits_frame, text="Writer/Illustrator: Kristina Balay")
writer_title.pack(side=TOP)
sound_title = Label(credits_frame, text="Sounds Provided By: http://www.soundjay.com/")
sound_title.pack(side=TOP)
back_button = Button(credits_frame, text="Back", command=back_to_menu)
back_button.pack(side=TOP)

#menu
new = Button(menu_frame, text="New Game", command=new_game)
new.pack(side=TOP)
load = Button(menu_frame, text="Load Game", command=load_game)
load.pack(side=TOP)
credits = Button(menu_frame, text="Credits", command=show_credits)
credits.pack(side=TOP)
warning = Label(menu_frame, text="This game has the potential to induce SEIZURES for people with Photosensitive Epilepsy")
warning.pack(side=BOTTOM)
warning_title = Label(menu_frame, text="Seizure Warning", foreground="red", font="-weight bold")
warning_title.pack(side=BOTTOM)

AB = ['.', '-', '|', '-', '.', '.', '.']
#blinker.flash(root, AB)
#root.after(400, blinker.flash, root, AB)
root.mainloop()