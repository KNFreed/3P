#imports
from tkinter import *
from tkinter import font
import random, os, time
from PIL import ImageTk

window = Tk()
window.title('3P! The Console')

### Window size
# Uncomment this one for a rasp install
#window.attributes('-fullscreen', True)
# Uncomment this one for a windows install
window.geometry("1200x600")

###Variables
#Clock variables
time1 = ''
updatedhour='None'
#Background color of the UI
main_background='#696969'
#Playbutton Background


### Making a grid to place objects
window.rowconfigure(0,weight=0)
window.rowconfigure(1,weight=1, uniform='semi')
window.rowconfigure(2,weight=1, uniform='semi')
window.columnconfigure(0,weight=1, uniform='third')
window.columnconfigure(1,weight=1, uniform='third')
window.columnconfigure(2,weight=1, uniform='third')

### Creating the infobar
canvas = Canvas(window, height=20, bg=main_background, bd=0, highlightthickness=0,)
canvas.grid(row=0, column=0, columnspan=3, sticky='EWNS')

### Creating the time widget
def tick():
    global time1, hour, updatedhour
    time2 = time.strftime('%H:%M')
    if time2 != time1:
        time1 = time2
        if updatedhour!='':
            canvas.delete(updatedhour)
            updatedhour = canvas.create_text(30, 10, text=time1, font="Helvetica", fill="white")
    window.after(1000, tick)
tick()

def menu():
    playfont = font.Font(family='Helvetica', size=40, weight='bold')
    ### Playbutton
    #Selects random background for the PlayButtonn
    path = r"./games/background/"
    greypath = r"./games/background/grey/"
    random_background = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
    background_path = str(path + random_background)
    greybackground_path = str(greypath + random_background)
    background = ImageTk.PhotoImage(master=window, file=background_path)
    greybackground = ImageTk.PhotoImage(master=window, file=greybackground_path)
    # Define the playbutton
    playbutton = Button(window, image=background, bd=0, highlightthickness=0, text="Play", font=playfont, fg="white", command=menu)
    playbutton.grid(row=1, column=0, columnspan=2, sticky='EWNS')
    # Hover function
    def playbuttonhover(e):
        playbutton['image'] = greybackground
    def playbuttonunhover(e):
        playbutton['image'] = background
    playbutton.bind("<Enter>", playbuttonhover)
    playbutton.bind("<Leave>", playbuttonunhover)

    ### Settingsbutton

    # Define the playbutton
    settingsbutton = Button(window, bg="#f57270", bd=0, highlightthickness=0, text="Settings", font=playfont, fg="white")
    settingsbutton.grid(row=2, column=2, columnspan=1, sticky='EWNS')
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
    newsbutton.grid(row=2, column=0, columnspan=1, sticky='EWNS')
    # Hover function
    def newsbuttonhover(e):
        newsbutton['bg'] = '#2d9f3c'
    def newsbuttonunhover(e):
        newsbutton['bg'] = '#60d26f'
    newsbutton.bind("<Enter>", newsbuttonhover)
    newsbutton.bind("<Leave>", newsbuttonunhover)

    ### abutton
    abutton = Button(window, bg="#ffbe4d", bd=0, highlightthickness=0, text="A button", font=playfont, fg="white")
    abutton.grid(row=2, column=1, columnspan=1, sticky='EWNS')

    def abuttonhover(e):
        abutton['bg'] = '#e69100'

    def abuttonunhover(e):
        abutton['bg'] = '#ffbe4d'

    abutton.bind("<Enter>", abuttonhover)
    abutton.bind("<Leave>", abuttonunhover)

    ### Appsbutton
    appsbutton = Button(window, bg="#16e6e9", bd=0, highlightthickness=0, text="Apps", font=playfont, fg="white")
    appsbutton.grid(row=1, column=2, columnspan=1, sticky='EWNS')

    def appsbuttonhover(e):
        appsbutton['bg'] = '#10aeb0'

    def appsbuttonunhover(e):
        appsbutton['bg'] = '#16e6e9'

    appsbutton.bind("<Enter>", appsbuttonhover)
    appsbutton.bind("<Leave>", appsbuttonunhover)
menu()
window.mainloop()
