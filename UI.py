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

### Background color and images
def lightmodeon():
    global textcolor, backgroundcolor, infobarbackground, apps_hoverDI, appsDI, news_hoverDI, newsDI, play_hoverDI, playDI, settings_hoverDI, settingsDI, shutdown_hoverDI, shutdownDI
    backgroundcolor = 'white'
    textcolor = "#464d59"
    infobarbackground = "white"
    window.configure(background=backgroundcolor)
    # Light Images
    appsDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Light/apps.png")
    newsDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Light/news.png")
    playDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Light/play.png")
    settingsDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Light/settings.png")
    shutdownDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Light/shutdown.png")
    apps_hoverDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Light/Hover/apps_hover.png")
    news_hoverDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Light/Hover/news_hover.png")
    settings_hoverDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Light/Hover/settings_hover.png")
    shutdown_hoverDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Light/Hover/shutdown_hover.png")
    if os.path.isfile('./files/easteregg'):
        play_hoverDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Light/Hover/play_hover_easteregg.png")
    else:
        play_hoverDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Light/Hover/play_hover.png")

def darkmodeon():
    global textcolor, backgroundcolor, infobarbackground, apps_hoverDI, appsDI, news_hoverDI, newsDI, play_hoverDI, playDI, settings_hoverDI, settingsDI, shutdown_hoverDI, shutdownDI
    backgroundcolor = '#464d59'
    infobarbackground = "#464d59"
    textcolor = "white"
    window.configure(background=backgroundcolor)
    # Dark Images
    appsDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Dark/apps.png")
    newsDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Dark/news.png")
    playDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Dark/play.png")
    settingsDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Dark/settings.png")
    shutdownDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Dark/shutdown.png")
    apps_hoverDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Dark/Hover/apps_hover.png")
    news_hoverDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Dark/Hover/news_hover.png")
    settings_hoverDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Dark/Hover/settings_hover.png")
    shutdown_hoverDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Dark/Hover/shutdown_hover.png")
    if os.path.isfile('./files/easteregg'):
        play_hoverDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Dark/Hover/play_hover_easteregg.png")
    else:
        play_hoverDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Dark/Hover/play_hover.png")

if os.path.isfile('./files/light'):
    lightmodeon()
else:
    darkmodeon()

### Creating the infobar
canvas = Canvas(window, height=30, bg=infobarbackground, bd=0, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3, sticky='EWNS')

### Creating the time widget
def tick():
    global time1, hour, updatedhour
    time2 = time.strftime('%H:%M')
    if time2 != time1:
        time1 = time2
        if updatedhour!='':
            canvas.delete(updatedhour)
            updatedhour = canvas.create_text(30, 15, text=time1, font=("Helvetica", 15), fill=textcolor)
    window.after(1000, tick)
tick()

def stop():
    os.system("sudo shutdown -h now")

### UI
def menu():
    configure()
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
    hoverpath = r"./games/background/Hover/"
    nbackgrounds = os.path.isfile("./files/backgrounds")
    if nbackgrounds:
        random_background = random.choice([
            x for x in os.listdir(path)
            if os.path.isfile(os.path.join(path, x))
        ])
        background_path = str(path + random_background)
        hoverbackground_path = str(hoverpath + random_background)
        playbackground = ImageTk.PhotoImage(master=window, file=background_path)
        playhoverbackground = ImageTk.PhotoImage(master=window, file=hoverbackground_path)
    else:
        playbackground = playDI
        playhoverbackground = play_hoverDI
    # Define the playbutton
    playbutton = Button(window, image=playbackground, bd=0, highlightthickness=0, command=menu)
    playbutton.grid(row=1, column=0, columnspan=2, sticky='EWNS')
    # Hover function
    def playbuttonhover(e):
        playbutton['image'] = playhoverbackground
    def playbuttonunhover(e):
        playbutton['image'] = playbackground
    playbutton.bind("<Enter>", playbuttonhover)
    playbutton.bind("<Leave>", playbuttonunhover)

    ### stopbutton

    # Define the stopbutton
    stopbutton = Button(window, image=shutdownDI, bd=0, highlightthickness=0, command=stop)
    stopbutton.grid(row=2, column=2, columnspan=1, sticky='EWNS')
    # Hover function
    def stopbuttonhover(e):
        stopbutton['image'] = shutdown_hoverDI
    def stopbuttonunhover(e):
        stopbutton['image'] = shutdownDI
    stopbutton.bind("<Enter>", stopbuttonhover)
    stopbutton.bind("<Leave>", stopbuttonunhover)

    ### Newsbutton

    # Define the newsbutton
    newsbutton = Button(window, image=newsDI, bd=0, highlightthickness=0, command=destroymenu)
    newsbutton.grid(row=2, column=0, columnspan=1, sticky='EWNS')
    # Hover function
    def newsbuttonhover(e):
        newsbutton['image'] = news_hoverDI
    def newsbuttonunhover(e):
        newsbutton['image'] = newsDI
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
        canvas.grid(row=0, column=0, columnspan=3, sticky='EWNS')

        # Title Canvas
        title_canvas = Canvas(window, bg="#ffbe4d", bd=0, highlightthickness=0)
        title_canvas.create_text(400, 47.5, font=(playfont, 35), text="Settings", fill="white")
        title_canvas.grid(row=1, column=1, columnspan=2, sticky='EWNS')

        #Return button
        def returnmenu():
            title_canvas.destroy()
            returnbutton.destroy()
            exitprog_settings.destroy()
            colormode_settings.destroy()
            menu()

        def switchmode():
            def exitswitchmode():
                newindow.destroy()

            newindow = Canvas(window, bg=backgroundcolor, bd=0, highlightthickness=0)
            newindow.grid(row=1, column=0, columnspan=3, rowspan=7, sticky="EWNS")

            def darkmodechoice():
                darkmodeon()
                if os.path.isfile('./files/light'):
                    os.remove("./files/light")
                exitswitchmode()
                returnmenu()

            def lightmodechoice():
                lightmodeon()
                open("./files/light", "w+")
                exitswitchmode()
                returnmenu()

            def eastereggchoice():
                global play_hoverDI, eastereggon
                if os.path.isfile('./files/easteregg'):
                    os.remove("./files/easteregg")
                    if os.path.isfile('./files/light'):
                        play_hoverDI = ImageTk.PhotoImage(master=window,
                                                          file="./files/Menu/Light/Hover/play_hover.png")
                    else:
                        play_hoverDI = ImageTk.PhotoImage(master=window,
                                                          file="./files/Menu/Dark/Hover/play_hover.png")
                    easteregg['text'] = "Easter Egg is off!"
                else:
                    open("./files/easteregg", "w+")
                    if os.path.isfile('./files/light'):
                        play_hoverDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Light/Hover/play_hover_easteregg.png")
                    else:
                        play_hoverDI = ImageTk.PhotoImage(master=window, file="./files/Menu/Dark/Hover/play_hover_easteregg.png")
                    easteregg['text'] = "Easter Egg is on!"

            returntosettings = Button(window, bd=0, highlightthickness=0, text="Return", font=playfont, fg=textcolor,
                              command=exitswitchmode, bg=backgroundcolor, anchor="center")
            returntosettings_window = newindow.create_window(600, 580, anchor=S, window=returntosettings)

            darkmode = Button(window, bd=0, highlightthickness=0, text="Dark Mode", font=playfont, fg=textcolor,
                                      command=darkmodechoice, bg=backgroundcolor, anchor="center")
            darkmode_window = newindow.create_window(200, 300, anchor=S, window=darkmode)

            lightmode = Button(window, bd=0, highlightthickness=0, text="Light Mode", font=playfont, fg=textcolor,
                              command=lightmodechoice, bg=backgroundcolor, anchor="center")
            lightmode_window = newindow.create_window(1000, 300, anchor=S, window=lightmode)

            easteregg = Button(window, bd=0, highlightthickness=0, font=playfont, fg=textcolor,
                               command=eastereggchoice, bg=backgroundcolor, anchor="center")
            easteregg_window = newindow.create_window(600, 150, anchor=S, window=easteregg)

            if os.path.isfile('./files/easteregg'):
                easteregg['text'] = "Easter Egg is on!"
            else:
                easteregg['text'] = ""

        returnbutton = Button(window, bd=0, highlightthickness=0, text="Return", font=playfont, fg="white", command=returnmenu, bg="orange")
        returnbutton.grid(row=1, column=0, columnspan=1, sticky='EWNS')

        colormode_settings = Button(window, bd=2, highlightthickness=0, text="Switch Dark/Light mode", font=playfont, fg=textcolor,
                              command=switchmode, bg=backgroundcolor, anchor="w")
        colormode_settings.grid(row=2, column=0, columnspan=3, sticky='EWNS')

        def exitprog():
            sys.exit()
        exitprog_settings = Button(window, bd=2, highlightthickness=0, text="Exit Prog", font=playfont, fg=textcolor, command=exitprog, bg=backgroundcolor, anchor="w")
        exitprog_settings.grid(row=6, column=2, columnspan=1, sticky='EWNS')

    settingsbutton = Button(window, image=settingsDI, bd=0, highlightthickness=0, command=settings)
    settingsbutton.grid(row=2, column=1, columnspan=1, sticky='EWNS')

    def settingsbuttonhover(e):
        settingsbutton['image'] = settings_hoverDI

    def settingsbuttonunhover(e):
        settingsbutton['image'] = settingsDI

    settingsbutton.bind("<Enter>", settingsbuttonhover)
    settingsbutton.bind("<Leave>", settingsbuttonunhover)

    ### Appsbutton
    appsbutton = Button(window, image=appsDI, bd=0, highlightthickness=0)
    appsbutton.grid(row=1, column=2, columnspan=1, sticky='EWNS')

    def appsbuttonhover(e):
        appsbutton['image'] = apps_hoverDI

    def appsbuttonunhover(e):
        appsbutton['image'] = appsDI

    appsbutton.bind("<Enter>", appsbuttonhover)
    appsbutton.bind("<Leave>", appsbuttonunhover)
menu()
window.mainloop()