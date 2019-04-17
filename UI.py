#imports
from tkinter import *
from tkinter import font
import random, os, time, sys
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


### Making a grid to place objects
def configure():
    window.rowconfigure(0,weight=0)
    window.rowconfigure(1,weight=1, uniform='semi')
    window.rowconfigure(2,weight=1, uniform='semi')
    window.columnconfigure(0,weight=1, uniform='third')
    window.columnconfigure(1,weight=1, uniform='third')
    window.columnconfigure(2,weight=1, uniform='third')
configure()

### Creating variables for the background color

light = os.path.isfile('./files/light')
if light:
    backgroundcolor = 'white'
    textcolor = "black"
    infobarbackground = "#4f4f4f"
    window.configure(background=backgroundcolor)
else:
    backgroundcolor = '#696969'
    infobarbackground = "#4f4f4f"
    textcolor = "white"
    window.configure(background=backgroundcolor)

### Creating the infobar
canvas = Canvas(window, height=20, bg=infobarbackground, bd=0, highlightthickness=0)
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

def stop():
    os.system("sudo shutdown -h now")

### UI
def menu():
    configure()
    canvas.grid(row=0, column=0, columnspan=6, sticky='EWNS')
    # Useful defs
    def destroymenu():
        playbutton.destroy()
        stopbutton.destroy()
        newsbutton.destroy()
        settingsbutton.destroy()
        appsbutton.destroy()
    # Menu UI
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

    ### stopbutton

    # Define the stopbutton
    stopbutton = Button(window, bg="#f57270", bd=0, highlightthickness=0, text="Power off", font=playfont, fg="white", command=stop)
    stopbutton.grid(row=2, column=2, columnspan=1, sticky='EWNS')
    # Hover function
    def stopbuttonhover(e):
        stopbutton['bg'] = '#f02c28'
    def stopbuttonunhover(e):
        stopbutton['bg'] = '#f57270'
    stopbutton.bind("<Enter>", stopbuttonhover)
    stopbutton.bind("<Leave>", stopbuttonunhover)

    ### Newsbutton

    def news():
        destroymenu()

    ## Config

        window.rowconfigure(0, weight=0)
        window.rowconfigure(1, weight=1, uniform='row')
        window.rowconfigure(2, weight=1, uniform='row')
        window.rowconfigure(3, weight=1, uniform='row')
        window.rowconfigure(4, weight=1, uniform='row')
        window.rowconfigure(5, weight=1, uniform='row')
        window.columnconfigure(0, weight=1, uniform='column')
        window.columnconfigure(1, weight=1, uniform='column')
        window.columnconfigure(2, weight=1, uniform='column')
        window.columnconfigure(3, weight=1, uniform='column')
        window.columnconfigure(4, weight=1, uniform='column')
        window.columnconfigure(5, weight=1, uniform='column')

    ## Interface

    # Title Canvas
    tcanvas = Canvas(window, bg="#2d9f3c", bd=0, highlightthickness=0)
    tcanvas.create_text(500, 47.5, font=("Papyrus", 26), text="News", fill="black")
    tcanvas.grid(row=1, column=0, columnspan=6, sticky='EWNS')

    # Frames

    fpicture = Frame(window, borderwidth=2, bg="#2b2f37", relief=GROOVE)
    fpicture.grid(row=2, column=0, rowspan=3, columnspan=3, sticky='EWNS')
    Label(fpicture, text='Picture').pack(anchor='center')

    ftitlenews = Frame(window, borderwidth=2, bg="#2b2f37", relief=GROOVE)
    ftitlenews.grid(row=2, column=3, rowspan=1, columnspan=2, sticky='EWNS')
    Label(ftitlenews, text='Title of News').pack(anchor='center')

    fdescription = Frame(window, borderwidth=2, bg="#2b2f37", relief=GROOVE)
    fdescription.grid(row=3, column=3, rowspan=3, columnspan=2, sticky='EWNS')
    Label(fdescription, text='Description').pack(anchor='center')

    # Button

    bnextnew = Button(window, relief=GROOVE, bg="#2b2f37", text='Next New', fg='white')
    bnextnew.grid(row=2, column=5, rowspan=4, sticky='EWNS')

    breturn = Button(window, relief=GROOVE, bg="#2b2f37", text='Return', fg='white')
    breturn.grid(row=5, column=0, columnspan=3, sticky='EWNS')

    # Define the newsbutton
    newsbutton = Button(window, bg="#60d26f", bd=0, highlightthickness=0, text="News", font=playfont,fg="white", command=destroymenu)
    newsbutton.grid(row=2, column=0, columnspan=1, sticky='EWNS')
    # Hover function
    def newsbuttonhover(e):
        newsbutton['bg'] = '#2d9f3c'
    def newsbuttonunhover(e):
        newsbutton['bg'] = '#60d26f'
    newsbutton.bind("<Enter>", newsbuttonhover)
    newsbutton.bind("<Leave>", newsbuttonunhover)

    ### settingsbutton

    def settings():
        # Destroy all the buttons that existed
        destroymenu()

        #configure the grid
        window.rowconfigure(0, weight=0)
        window.rowconfigure(1, weight=1, uniform='fifth')
        window.rowconfigure(2, weight=1, uniform='fifth')
        window.rowconfigure(3, weight=1, uniform='fifth')
        window.rowconfigure(4, weight=1, uniform='fifth')
        window.rowconfigure(5, weight=1, uniform='fifth')
        window.rowconfigure(6, weight=1, uniform='fifth')
        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=1, uniform='sixth')
        window.columnconfigure(2, weight=1, uniform='sixth')
        canvas.grid(row=0, column=0, columnspan=3, sticky='EWNS')

        # Title Canvas
        title_canvas = Canvas(window, bg="#ffbe4d", bd=0, highlightthickness=0)
        title_canvas.create_text(400, 47.5, font=(playfont, 35), text="Settings", fill="white")
        title_canvas.grid(row=1, column=1, columnspan=2, sticky='EWNS')

        #Return button
        def returnmenu():
            title_canvas.destroy()
            returnbutton.destroy()
            menu()

        def switchmode():
            def exitswitchmode():
                newindow.destroy()
            newindow = Canvas(window, bg=backgroundcolor, bd=0, highlightthickness=0)
            newindow.grid(row=1, column=0, columnspan=3, rowspan=7, sticky="EWNS")

            def darkmodechoice():
                global backgroundcolor, textcolor
                backgroundcolor = '#696969'
                textcolor = "white"
                window.configure(background=backgroundcolor)
                if light:
                    os.remove("./files/light")
                exitswitchmode()
                returnmenu()

            def lightmodechoice():
                global backgroundcolor, textcolor
                backgroundcolor = 'white'
                textcolor = "black"
                window.configure(background=backgroundcolor)
                open("./files/light", "w+")
                exitswitchmode()
                returnmenu()

            returntosettings = Button(window, bd=0, highlightthickness=0, text="Return", font=playfont, fg=textcolor,
                              command=exitswitchmode, bg=backgroundcolor, anchor="center")
            returntosettings_window = newindow.create_window(600, 580, anchor=S, window=returntosettings)

            darkmode = Button(window, bd=0, highlightthickness=0, text="Dark Mode", font=playfont, fg=textcolor,
                                      command=darkmodechoice, bg=backgroundcolor, anchor="center")
            darkmode_window = newindow.create_window(200, 300, anchor=S, window=darkmode)

            lightmode = Button(window, bd=0, highlightthickness=0, text="Light Mode", font=playfont, fg=textcolor,
                              command=lightmodechoice, bg=backgroundcolor, anchor="center")
            lightmode_window = newindow.create_window(1000, 300, anchor=S, window=lightmode)

        returnbutton = Button(window, bd=0, highlightthickness=0, text="Return", font=playfont, fg="white", command=returnmenu, bg="orange")
        returnbutton.grid(row=1, column=0, columnspan=1, sticky='EWNS')

        colormode_settings = Button(window, bd=2, highlightthickness=0, text="Switch Dark/Light mode", font=playfont, fg=textcolor,
                              command=switchmode, bg=backgroundcolor, anchor="w")
        colormode_settings.grid(row=2, column=0, columnspan=3, sticky='EWNS')

    settingsbutton = Button(window, bg="#ffbe4d", bd=0, highlightthickness=0, text="Settings", font=playfont, fg="white", command=settings)
    settingsbutton.grid(row=2, column=1, columnspan=1, sticky='EWNS')

    def settingsbuttonhover(e):
        settingsbutton['bg'] = '#e69100'

    def settingsbuttonunhover(e):
        settingsbutton['bg'] = '#ffbe4d'

    settingsbutton.bind("<Enter>", settingsbuttonhover)
    settingsbutton.bind("<Leave>", settingsbuttonunhover)

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
