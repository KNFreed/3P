#imports
from tkinter import *
from tkinter import font
import random, os
from PIL import ImageTk

window = Tk()
window.title('3P! The Console')
window.attributes('-fullscreen', True)
window.rowconfigure((0,1), weight=1)
window.columnconfigure(0,weight=1, uniform='third')
window.columnconfigure(1,weight=1, uniform='third')
window.columnconfigure(2,weight=1, uniform='third')

# variables for the play button background
path = r"./games/background/"
random_background = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])
background_path = str(path+random_background)
background = ImageTk.PhotoImage(master=window, file=background_path)

def selectbackground():
    global path, random_background, background_path, background
    random_background = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    background_path = str(path + random_background)
    background = ImageTk.PhotoImage(master=window, file=background_path)

def menu():
    playfont = font.Font(family='Helvetica', size=40, weight='bold')
    ### Playbutton

    # Select the button background
    selectbackground()
    # Define the playbutton
    playbutton = Button(window, image=background, bd=0, highlightthickness=0, text="Play", font=playfont, fg="white", command=menu)
    playbutton.grid(row=0, column=0, columnspan=2, sticky='EWNS')
    # Hover function
    def playbuttonhover(e):
        playbutton['bg'] = '#990099'
    def playbuttonunhover(e):
        playbutton['bg'] = '#ab4bb4'
    playbutton.bind("<Enter>", playbuttonhover)
    playbutton.bind("<Leave>", playbuttonunhover)

    ### Settingsbutton

    # Define the playbutton
    settingsbutton = Button(window, bg="#f57270", bd=0, highlightthickness=0, text="Settings", font=playfont, fg="white")
    settingsbutton.grid(row=1, column=2, columnspan=1, sticky='EWNS')
    # Hover function
    def settingsbuttonhover(e):
        settingsbutton['bg'] = '#f02c28'
    def settingsbuttonunhover(e):
        settingsbutton['bg'] = '#f57270'
    settingsbutton.bind("<Enter>", settingsbuttonhover)
    settingsbutton.bind("<Leave>", settingsbuttonunhover)

    ### Newsbutton

    # Define the newsbutton
    newsbutton = Button(window, bg="#60d26f", bd=0, highlightthickness=0, text="News", font=playfont,fg="white")
    newsbutton.grid(row=1, column=0, columnspan=1, sticky='EWNS')
    # Hover function
    def newsbuttonhover(e):
        newsbutton['bg'] = '#2d9f3c'
    def newsbuttonunhover(e):
        newsbutton['bg'] = '#60d26f'
    newsbutton.bind("<Enter>", newsbuttonhover)
    newsbutton.bind("<Leave>", newsbuttonunhover)

    ### abutton
    abutton = Button(window, bg="#ffbe4d", bd=0, highlightthickness=0, text="A button", font=playfont, fg="white")
    abutton.grid(row=1, column=1, columnspan=1, sticky='EWNS')

    def abuttonhover(e):
        abutton['bg'] = '#e69100'

    def abuttonunhover(e):
        abutton['bg'] = '#ffbe4d'

    abutton.bind("<Enter>", abuttonhover)
    abutton.bind("<Leave>", abuttonunhover)

    ### bbutton
    bbutton = Button(window, bg="#16e6e9", bd=0, highlightthickness=0, text="B button", font=playfont, fg="white")
    bbutton.grid(row=0, column=2, columnspan=1, sticky='EWNS')

    def bbuttonhover(e):
        bbutton['bg'] = '#10aeb0'

    def bbuttonunhover(e):
        bbutton['bg'] = '#16e6e9'

    bbutton.bind("<Enter>", bbuttonhover)
    bbutton.bind("<Leave>", bbuttonunhover)
menu()
window.mainloop()