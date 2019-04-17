# imports
from tkinter import *
from tkinter import font
import random, os, time, sys, sqlite3
from PIL import ImageTk

window = Tk()
window.title('3P! The Console')

### Window size
# Uncomment this one for a rasp install
# window.attributes('-fullscreen', True)
# Uncomment this one for a windows install
window.geometry("1024x600")

###Variables
# Clock variables
time1 = ''
updatedhour = 'None'
# Used variables for the login page
logo = ImageTk.PhotoImage(master=window, file="./files/logo.png")
backgroundcolor = '#464d59'
infobarbackground = "#464d59"
textcolor = "white"
disconnect = 0
### Making a grid to place objects
def configure():
    window.rowconfigure(0, weight=0)
    window.rowconfigure(1, weight=1, uniform='semi')
    window.rowconfigure(2, weight=1, uniform='semi')
    window.columnconfigure(0, weight=1, uniform='third')
    window.columnconfigure(1, weight=1, uniform='third')
    window.columnconfigure(2, weight=1, uniform='third')


configure()


### Background color and images
def lightmodeon():
    global textcolor, backgroundcolor, infobarbackground, apps_hoverDI, appsDI, news_hoverDI, newsDI, playDI, settings_hoverDI, settingsDI, shutdown_hoverDI, shutdownDI
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


def darkmodeon():
    global textcolor, backgroundcolor, infobarbackground, apps_hoverDI, appsDI, news_hoverDI, newsDI, playDI, settings_hoverDI, settingsDI, shutdown_hoverDI, shutdownDI
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


### Creating the infobar
canvas = Canvas(window, height=30, bg=infobarbackground, bd=0, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3, sticky='EWNS')


### Creating the time widget
def tick():
    global time1, updatedhour
    time2 = time.strftime('%H:%M')
    if time2 != time1:
        time1 = time2
        if updatedhour != '':
            canvas.delete(updatedhour)
            updatedhour = canvas.create_text(30, 15, text=time1, font=("Helvetica", 15), fill=textcolor)
    window.after(1000, tick)


tick()


# Stops the Rpi
def shutdown():
    os.system("sudo shutdown -h now")


# Stocks version
storeversion = open("./files/version", "r")
storedversion = storeversion.readline()
storedlastupdated = storeversion.readline()
storeversion.close()


### Login/Signup
def login():
    global curs, conn, updatedhour, play_hoverDI
    # Check if an account was already created. If yes, show login page
    if os.path.isfile('./files/account.db'):
        ### Create a Login/Register page
        signinup = Canvas(window, bg=backgroundcolor, bd=0, highlightthickness=0)
        signinup.grid(row=1, column=0, columnspan=3, rowspan=7, sticky="EWNS")
        conn = sqlite3.connect("./files/account.db")
        curs = conn.cursor()
        curs.execute("Select * from Accounts where kmli = 1")
        kmlicheck = curs.fetchone()

        # Create a new account
        def newaccount():
            signinbutton.destroy()
            newaccountbutton.destroy()
            # Those tries are made to delete errors if previously created
            try:
                if nicknamerror:
                    signinup.delete(nicknamerror)
            except:
                pass
            try:
                if passworderror:
                    signinup.delete(passworderror)
            except:
                pass
            try:
                if kmlierror:
                    signinup.delete(kmlierror)
            except:
                pass

            def goback():
                signinup.destroy()
                login()

            def newacc():
                global play_hoverDI
                nick = nickinput.get()
                pwd = pwdinput.get()
                kmli = kmliinput.get()
                curs.execute("Select * from Accounts where nickname = ?", (nick,))
                nickcheck = curs.fetchone()

                # Verify if the nickname isn't already used
                if nickcheck is None:

                    # Verify if a password and a nick were written. Made so an account must have a password.
                    if nick != "" and pwd != "":
                        curs.execute("Select nickname from Accounts where kmli = 1")
                        kmlicheck = curs.fetchone()
                        if kmlicheck != "" and kmli == 1:
                            kmlierror = signinup.create_text(512, 320,
                                                                text="You can't have 2 accounts automatically logged at the same time.",
                                                                font=("Helvetica", 10), fill="red")
                        else:
                            newaccount = [(nick, pwd, kmli, 0, 0, 0)]
                            curs.execute("INSERT INTO Accounts VALUES(?,?,?,?,?,?)", newaccount[0])
                            conn.commit()
                            darkmodeon()
                            play_hoverDI = ImageTk.PhotoImage(master=window,
                                                              file="./files/Menu/Dark/Hover/play_hover.png")
                            signinup.destroy()
                            menu(nick)
                    else:
                        error = signinup.create_text(512, 370, text="Please enter a nickname and a password.",
                                                     font=("Helvetica", 10), fill="red")

                else:
                    nicknamerror = signinup.create_text(512, 320, text="Username already exists. please try again.",
                                                        font=("Helvetica", 10), fill="red")

            # signinin Button
            signupbutton = Button(window, bd=0, highlightthickness=0, text="Sign up", fg=textcolor, bg=backgroundcolor,
                                  anchor="center", command=newacc)
            signupbutton_window = signinup.create_window(512, 480, anchor=S, window=signupbutton)

            # new account Button
            gobackbutton = Button(window, bd=0, highlightthickness=0, text="Already have an account ?", fg=textcolor,
                                  bg=backgroundcolor,
                                  anchor="center", command=goback)
            gobackbutton_window = signinup.create_window(512, 500, anchor=S, window=gobackbutton)

        # Sign in into an existing account
        def signin():
            global updatedhour, play_hoverDI, passworderror
            nick = nickinput.get()
            pwd = pwdinput.get()
            kmli = kmliinput.get()
            curs.execute("Select * from Accounts where nickname = ?", (nick,))
            check1 = curs.fetchone()

            #Check if the nickname written exists in the database.
            if check1 is None:
                global nicknamerror, kmlierror
                nicknamerror = signinup.create_text(512, 320, text="This user doesn't exist", font=("Helvetica", 10),
                                                    fill="red")
            else:
                # Delete the error after entering a correct nickname
                try:
                    if nicknamerror:
                        signinup.delete(nicknamerror)
                except:
                    pass
                curs.execute("Select * from Accounts where password = ? and nickname = ?", (pwd, nick))
                check2 = curs.fetchone()

                #Check if the password is correct
                if check2 is None:
                    passworderror = signinup.create_text(512, 370, text="Wrong password. Please Try again.",
                                                         font=("Helvetica", 10), fill="red")
                else:
                    curs.execute("Select nickname from Accounts where kmli = 1")
                    kmlicheck = curs.fetchone()
                    if kmlicheck is not None and kmli == 1:
                        kmlierror = signinup.create_text(512, 320,
                                                                text="You can't have 2 accounts automatically logged at the same time.",
                                                                font=("Helvetica", 10), fill="red")
                    else:
                        signinup.destroy()
                        curs.execute("Update Accounts SET kmli = ? WHERE nickname = ?", (kmli, nick))
                        conn.commit()
                        # Check what mode is enabled
                        curs.execute("Select * from Accounts where light = 1 and nickname = ?", (nick,))
                        checklightmode = curs.fetchone()

                        # Check if lightmode is on for that user
                        if checklightmode:
                            lightmodeon()
                            curs.execute("Select * from Accounts where easteregg = 1 and nickname = ?", (nick,))
                            checkeasteregg = curs.fetchone()

                            # Check if easteregg is on for that user
                            if checkeasteregg:
                                play_hoverDI = ImageTk.PhotoImage(master=window,
                                                                  file="./files/Menu/Light/Hover/play_hover_easteregg.png")
                            else:
                                play_hoverDI = ImageTk.PhotoImage(master=window,
                                                                  file="./files/Menu/Light/Hover/play_hover.png")
                            canvas['bg'] = infobarbackground
                            canvas.delete(updatedhour)
                            updatedhour = canvas.create_text(30, 15, text=time1, font=("Helvetica", 15), fill=textcolor)
                        else:
                            darkmodeon()
                            curs.execute("Select * from Accounts where easteregg = 1 and nickname = ?", (nick,))
                            checkeasteregg = curs.fetchone()
                            if checkeasteregg:
                                play_hoverDI = ImageTk.PhotoImage(master=window,
                                                                  file="./files/Menu/Dark/Hover/play_hover_easteregg.png")
                            else:
                                play_hoverDI = ImageTk.PhotoImage(master=window,
                                                                  file="./files/Menu/Dark/Hover/play_hover.png")
                            canvas['bg'] = infobarbackground
                            canvas.delete(updatedhour)
                            updatedhour = canvas.create_text(30, 15, text=time1, font=("Helvetica", 15), fill=textcolor)
                        signinup.destroy()
                        menu(nick)

        # Check if "Keep me logged in" button was checked, if so, connects automatically
        if kmlicheck and disconnect == 0:
            curs.execute("Select nickname from Accounts where kmli = 1")
            nickname = curs.fetchone()
            nick = nickname[0]
            # Check what mode is enabled
            curs.execute("Select * from Accounts where light = 1 and nickname = ?", (nick,))
            checklightmode = curs.fetchone()

            # Check if lightmode is on for that user
            if checklightmode:
                lightmodeon()
                curs.execute("Select * from Accounts where easteregg = 1 and nickname = ?", (nick,))
                checkeasteregg = curs.fetchone()

                # Check if easteregg is on for that user
                if checkeasteregg:
                    play_hoverDI = ImageTk.PhotoImage(master=window,
                                                      file="./files/Menu/Light/Hover/play_hover_easteregg.png")
                else:
                    play_hoverDI = ImageTk.PhotoImage(master=window,
                                                      file="./files/Menu/Light/Hover/play_hover.png")
                canvas['bg'] = infobarbackground
                canvas.delete(updatedhour)
                updatedhour = canvas.create_text(30, 15, text=time1, font=("Helvetica", 15), fill=textcolor)
            else:
                darkmodeon()
                curs.execute("Select * from Accounts where easteregg = 1 and nickname = ?", (nick,))
                checkeasteregg = curs.fetchone()
                if checkeasteregg:
                    play_hoverDI = ImageTk.PhotoImage(master=window,
                                                      file="./files/Menu/Dark/Hover/play_hover_easteregg.png")
                else:
                    play_hoverDI = ImageTk.PhotoImage(master=window,
                                                      file="./files/Menu/Dark/Hover/play_hover.png")
                canvas['bg'] = infobarbackground
                canvas.delete(updatedhour)
                updatedhour = canvas.create_text(30, 15, text=time1, font=("Helvetica", 15), fill=textcolor)
            signinup.destroy()
            menu(nick)

        else:
            # signinin Button
            signinbutton = Button(window, bd=0, highlightthickness=0, text="Sign in", fg=textcolor, bg=backgroundcolor,
                                  anchor="center", command=signin)
            signinbutton_window = signinup.create_window(512, 480, anchor=S, window=signinbutton)

            # new account Button
            newaccountbutton = Button(window, bd=0, highlightthickness=0, text="Create a New account", fg=textcolor,
                                      bg=backgroundcolor,
                                      anchor="center", command=newaccount)
            newaccountbutton_window = signinup.create_window(512, 500, anchor=S, window=newaccountbutton)

            # logo input
            signinup.create_image(512, 150, image=logo, anchor=CENTER)

            # Nick input
            nickinput = Entry(window)
            nickinput.insert(0, 'Nickname')
            nickinput_window = signinup.create_window(512, 350, anchor=S, window=nickinput)

            # Pwd input
            pwdinput = Entry(window)
            pwdinput.insert(0, 'Password')
            pwdinput_window = signinup.create_window(512, 400, anchor=S, window=pwdinput)

            kmliinput = IntVar()
            f = Frame(signinup)
            signinup.create_window((512, 420), window=f, anchor="n")
            Checkbutton(f, text="Keep me logged in", variable=kmliinput).pack()

    else:

        # Create a Register Page
        def signup():
            global play_hoverDI, curs, conn
            nick = nickinput.get()
            pwd = pwdinput.get()
            kmli = kmliinput.get()
            # Create a database
            conn = sqlite3.connect("./files/account.db")
            curs = conn.cursor()

            # Check if there is a password and a nickname written, if so, register it into the database and make it admin
            if nick != "" and pwd != "":
                curs.execute(
                    "CREATE TABLE Accounts(nickname TEXT,password TEXT,kmli INTEGER,light INTEGER,easteregg INTEGER,admin INTEGER)")
                newaccount = [(nick, pwd, kmli, 0, 0, 1)]
                curs.execute("INSERT INTO Accounts VALUES(?,?,?,?,?,?)", newaccount[0])
                conn.commit()
                darkmodeon()
                play_hoverDI = ImageTk.PhotoImage(master=window,
                                                  file="./files/Menu/Dark/Hover/play_hover.png")
                register.destroy()
                menu(nick)
            else:
                error = register.create_text(512, 370, text="Please enter a nickname and a password.",
                                             font=("Helvetica", 10), fill="red")

        # Canvas
        register = Canvas(window, bg=backgroundcolor, bd=0, highlightthickness=0)
        register.grid(row=1, column=0, columnspan=3, rowspan=7, sticky="EWNS")

        # register Button
        registerbutton = Button(window, bd=0, highlightthickness=0, text="Sign Up", fg=textcolor, bg=backgroundcolor,
                                anchor="center", command=signup)
        registerbutton_window = register.create_window(512, 480, anchor=S, window=registerbutton)

        # logo input
        register.create_image(512, 150, image=logo, anchor=CENTER)

        # Nick input
        nickinput = Entry(window)
        nickinput.insert(0, 'Nickname')
        nickinput_window = register.create_window(512, 350, anchor=S, window=nickinput)

        # Pwd input
        pwdinput = Entry(window)
        pwdinput.insert(0, 'Password')
        pwdinput_window = register.create_window(512, 400, anchor=S, window=pwdinput)

        kmliinput = IntVar()
        f = Frame(register)
        register.create_window((512, 420), window=f, anchor="n")
        Checkbutton(f, text="Keep me logged in", variable=kmliinput).pack()
        message = register.create_text(512, 320, text="This will be the Admin account", font=("Helvetica", 10),
                                       fill=textcolor)

### UI
def menu(nick):
    configure()
    welcome = "Welcome {}!".format(nick)
    welcometext = canvas.create_text(512, 15, text=welcome, font=("Helvetica", 15), fill=textcolor)

    ### Useful defs

    # Remove every button from the menu to leave a blank space for the next page
    def destroymenu():
        playbutton.destroy()
        shutdownbutton.destroy()
        newsbutton.destroy()
        settingsbutton.destroy()
        appsbutton.destroy()

    # Font used for some titles
    playfont = font.Font(family='Helvetica', size=40, weight='bold')

    # Selects random background for the PlayButton if there is one
    path = r"./games/background/"
    hoverpath = r"./games/background/Hover/"

    # Blank file that'll be written when a background will be installed
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

    ### Playbutton
    # Define the playbutton
    playbutton = Button(window, image=playbackground, relief=SOLID, bd=0, highlightthickness=0)
    playbutton.grid(row=1, column=0, columnspan=2, sticky='EWNS')

    # Hover function
    def playbuttonhover(e):
        playbutton['image'] = playhoverbackground

    def playbuttonunhover(e):
        playbutton['image'] = playbackground

    playbutton.bind("<Enter>", playbuttonhover)
    playbutton.bind("<Leave>", playbuttonunhover)

    ### shutdownbutton

    # Define the shutdownbutton
    shutdownbutton = Button(window, image=shutdownDI, bd=0, highlightthickness=0, command=shutdown, relief=FLAT)
    shutdownbutton.grid(row=2, column=2, columnspan=1, sticky='EWNS')

    # Hover function
    def shutdownbuttonhover(e):
        shutdownbutton['image'] = shutdown_hoverDI

    def shutdownbuttonunhover(e):
        shutdownbutton['image'] = shutdownDI

    shutdownbutton.bind("<Enter>", shutdownbuttonhover)
    shutdownbutton.bind("<Leave>", shutdownbuttonunhover)

    ### Newsbutton

    # Define the newsbutton
    newsbutton = Button(window, image=newsDI, bd=0, highlightthickness=0, command=destroymenu, relief=FLAT)
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
        global title_canvas
        # Destroy all the buttons that existed
        destroymenu()

        # configure the grid
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

        # Return button
        def returnmenu():
            title_canvas.destroy()
            returnbutton.destroy()
            exitprog_settings.destroy()
            colormode_settings.destroy()
            version_settings.destroy()
            changepassword_settings.destroy()
            disconnect_settings.destroy()
            try:
                if kmlichange_settings:
                    kmlichange_settings.destroy()
            except:
                pass
            try:
                if adminpanel_settings:
                    adminpanel_settings.destroy()
            except:
                pass

            menu(nick)

        def adminuser():
            title_canvas.destroy()
            returnbutton.destroy()
            exitprog_settings.destroy()
            colormode_settings.destroy()
            version_settings.destroy()
            changepassword_settings.destroy()
            disconnect_settings.destroy()
            adminpanel_settings.destroy()
            try:
                if kmlichange_settings:
                    kmlichange_settings.destroy()
            except:
                pass


            def returntosettings():
                admintitle_canvas.destroy()
                adminreturnbutton.destroy()
                changepwdbutton_admin.destroy()
                giveadmin_admin.destroy()
                settings()

            def adminchangepwd():
                admintitle_canvas.destroy()
                adminreturnbutton.destroy()
                changepwdbutton_admin.destroy()
                giveadmin_admin.destroy()

            def admingive():
                admintitle_canvas.destroy()
                adminreturnbutton.destroy()
                changepwdbutton_admin.destroy()
                giveadmin_admin.destroy()

            # Title Canvas
            admintitle_canvas = Canvas(window, bg="#ffbe4d", bd=0, highlightthickness=0)
            admintitle_canvas.create_text(400, 47.5, font=(playfont, 35), text="Account Management", fill="white")
            admintitle_canvas.grid(row=1, column=1, columnspan=2, sticky='EWNS')

            adminreturnbutton = Button(window, bd=0, highlightthickness=0, text="Return", font=playfont, fg="white",
                                  command=returntosettings, bg="orange")
            adminreturnbutton.grid(row=1, column=0, columnspan=1, sticky='EWNS')

            changepwdbutton_admin = Button(window, bd=0, highlightthickness=0, text="Change password of any account", font=playfont, fg=textcolor,
                                  command=adminchangepwd, bg=backgroundcolor)
            changepwdbutton_admin.grid(row=2, column=0, columnspan=3, sticky='EWNS')

            giveadmin_admin = Button(window, bd=0, highlightthickness=0, text="Give admin perms", font=playfont, fg=textcolor, command=admingive, bg=backgroundcolor)
            giveadmin_admin.grid(row=3, column=0, columnspan=3, sticky='EWNS')




        # Switch Dark/Light Button
        def switchmode():
            def exitswitchmode():
                newindow.destroy()

            # Create a blank space
            newindow = Canvas(window, bg=backgroundcolor, bd=0, highlightthickness=0)
            newindow.grid(row=1, column=0, columnspan=3, rowspan=7, sticky="EWNS")

            # Put everything into Dark Mode
            def darkmodechoice():
                global updatedhour, play_hoverDI
                darkmodeon()
                # Edit database to put the Dark Mode
                curs.execute("Update Accounts SET light = 0 WHERE nickname = ?", (nick,))
                conn.commit()
                canvas['bg'] = infobarbackground
                canvas.delete(updatedhour)
                updatedhour = canvas.create_text(30, 15, text=time1, font=("Helvetica", 15), fill=textcolor)
                curs.execute("Select * from Accounts where easteregg = 1 and nickname = ?", (nick,))
                checkeasteregg = curs.fetchone()
                if checkeasteregg:
                    play_hoverDI = ImageTk.PhotoImage(master=window,
                                                      file="./files/Menu/Dark/Hover/play_hover_easteregg.png")
                else:
                    play_hoverDI = ImageTk.PhotoImage(master=window,
                                                      file="./files/Menu/Dark/Hover/play_hover.png")
                exitswitchmode()
                returnmenu()

            # Put everything into Light Mode
            def lightmodechoice():
                global updatedhour, play_hoverDI
                lightmodeon()
                canvas['bg'] = infobarbackground
                # Edit database to ensure the light mode will stay even after a reboot
                curs.execute("Update Accounts SET light = 1 WHERE nickname = ?", (nick,))
                conn.commit()
                canvas.delete(updatedhour)
                updatedhour = canvas.create_text(30, 15, text=time1, font=("Helvetica", 15), fill=textcolor)
                curs.execute("Select * from Accounts where easteregg = 1 and nickname = ?", (nick,))
                checkeasteregg = curs.fetchone()
                if checkeasteregg:
                    play_hoverDI = ImageTk.PhotoImage(master=window,
                                                      file="./files/Menu/Light/Hover/play_hover_easteregg.png")
                else:
                    play_hoverDI = ImageTk.PhotoImage(master=window,
                                                      file="./files/Menu/Light/Hover/play_hover.png")

                exitswitchmode()
                returnmenu()

            # Enables Easter Egg
            def eastereggchoice():
                global play_hoverDI
                # Checks if Easter Egg is already enabled. If N: enable it. Y: Disable it.
                curs.execute("Select * from Accounts where easteregg = 1 and nickname = ?", (nick,))
                checkeasteregg = curs.fetchone()

                if checkeasteregg:
                    curs.execute("Update Accounts SET easteregg = 0 WHERE nickname = ?", (nick,))
                    conn.commit()
                    curs.execute("Select * from Accounts where light = 1 and nickname = ?", (nick,))
                    checklightmode = curs.fetchone()
                    if checklightmode:
                        play_hoverDI = ImageTk.PhotoImage(master=window,
                                                          file="./files/Menu/Light/Hover/play_hover.png")
                    else:
                        play_hoverDI = ImageTk.PhotoImage(master=window,
                                                          file="./files/Menu/Dark/Hover/play_hover.png")
                    easteregg['text'] = "Easter Egg is off!"

                else:
                    curs.execute("Update Accounts SET easteregg = 1 WHERE nickname = ?", (nick,))
                    conn.commit()
                    curs.execute("Select * from Accounts where light = 1 and nickname = ?", (nick,))
                    checklightmode = curs.fetchone()
                    if checklightmode:
                        play_hoverDI = ImageTk.PhotoImage(master=window,
                                                          file="./files/Menu/Light/Hover/play_hover_easteregg.png")
                    else:
                        play_hoverDI = ImageTk.PhotoImage(master=window,
                                                          file="./files/Menu/Dark/Hover/play_hover_easteregg.png")
                    easteregg['text'] = "Easter Egg is on!"

            # Choice buttons
            returntosettings = Button(window, bd=0, highlightthickness=0, text="Return", font=playfont, fg=textcolor,
                                      command=exitswitchmode, bg=backgroundcolor, anchor="center")
            returntosettings_window = newindow.create_window(512, 580, anchor=S, window=returntosettings)

            darkmode = Button(window, bd=0, highlightthickness=0, text="Dark Mode", font=playfont, fg=textcolor,
                              command=darkmodechoice, bg=backgroundcolor, anchor="center")
            darkmode_window = newindow.create_window(200, 350, anchor=S, window=darkmode)

            lightmode = Button(window, bd=0, highlightthickness=0, text="Light Mode", font=playfont, fg=textcolor,
                               command=lightmodechoice, bg=backgroundcolor, anchor="center")
            lightmode_window = newindow.create_window(800, 350, anchor=S, window=lightmode)

            easteregg = Button(window, bd=0, highlightthickness=0, font=playfont, fg=textcolor,
                               command=eastereggchoice, bg=backgroundcolor, anchor="center")
            easteregg_window = newindow.create_window(512, 150, anchor=S, window=easteregg)

            # Check if the Easter Egg is enabled when clicking on the Switcher
            curs.execute("Select * from Accounts where easteregg = 1 and nickname = ?", (nick,))
            checkeasteregg = curs.fetchone()

            # Check if easter egg is on
            if checkeasteregg:
                easteregg['text'] = "Easter Egg is on!"
            else:
                easteregg['text'] = ""

        def versionsettings():
            def exitversionsettings():
                newindow.destroy()

            # Create a blank space
            newindow = Canvas(window, bg=backgroundcolor, bd=0, highlightthickness=0)
            newindow.grid(row=1, column=0, columnspan=3, rowspan=7, sticky="EWNS")

            # Buttons
            returntosettings = Button(window, bd=0, highlightthickness=0, text="Return", font=playfont, fg=textcolor,
                                      command=exitversionsettings, bg=backgroundcolor, anchor="center")
            returntosettings_window = newindow.create_window(512, 580, anchor=S, window=returntosettings)

            newindow.create_image(512, 150, image=logo, anchor=CENTER)
            newindow.create_text(512, 350, font=(playfont, 20), text=storedversion, fill=textcolor)
            newindow.create_text(512, 400, font=(playfont, 20), text=storedlastupdated, fill=textcolor)

        def changepasswordsettings():
            def exitchangepasswordsetting():
                newindow.destroy()

            # Create a blank space
            newindow = Canvas(window, bg=backgroundcolor, bd=0, highlightthickness=0)
            newindow.grid(row=1, column=0, columnspan=3, rowspan=7, sticky="EWNS")

            def changepassword():
                global checkerror, pwderror, pwdchanged
                pwd = pwdinput.get()
                cpwd = cpwdinput.get()
                confirm = confirminput.get()
                if pwd == cpwd:
                    if confirm:
                        curs.execute("Update Accounts SET password = ? WHERE nickname = ?", (pwd, nick))
                        conn.commit()
                        try:
                            if checkerror:
                                newindow.delete(checkerror)
                        except:
                            pass
                        pwdchanged = newindow.create_text(512, 400,
                                                          text="Password changed. You will be redirected to the menu shortly.",
                                                          font=("Helvetica", 10), fill="red")
                        window.after(2000, exitchangepasswordsetting)
                    else:
                        try:
                            if pwderror:
                                newindow.delete(pwderror)
                        except:
                            pass
                        checkerror = newindow.create_text(512, 170,
                                                          text="Please check the box before updating the password.",
                                                          font=("Helvetica", 10), fill="red")
                else:
                    pwderror = newindow.create_text(512, 120,
                                                    text="Passwords are different. Please try again.",
                                                    font=("Helvetica", 10), fill="red")

            # Buttons
            returntosettings = Button(window, bd=0, highlightthickness=0, text="Return", font=playfont, fg=textcolor,
                                      command=exitchangepasswordsetting, bg=backgroundcolor, anchor="center")
            returntosettings_window = newindow.create_window(512, 580, anchor=S, window=returntosettings)

            # Pwd input
            pwdinput = Entry(window)
            pwdinput.insert(0, 'Nickname')
            pwdinput_window = newindow.create_window(512, 100, anchor=S, window=pwdinput)

            # Pwd input
            cpwdinput = Entry(window)
            cpwdinput.insert(0, 'Password')
            cpwdinput_window = newindow.create_window(512, 150, anchor=S, window=cpwdinput)

            confirminput = IntVar()
            f = Frame(newindow)
            newindow.create_window((512, 200), window=f, anchor="n")
            Checkbutton(f, text="Are you sure you want to change your password?", variable=confirminput).pack()

            # Buttons
            changepwd = Button(window, bd=0, highlightthickness=0, text="Change Password", font=playfont, fg=textcolor,
                               command=changepassword, bg=backgroundcolor, anchor="center")
            changepwd_window = newindow.create_window(512, 350, anchor=S, window=changepwd)

        def disconnectsettings():
            global disconnect, kmlichange_settings
            disconnect = 1
            title_canvas.destroy()
            returnbutton.destroy()
            exitprog_settings.destroy()
            colormode_settings.destroy()
            version_settings.destroy()
            changepassword_settings.destroy()
            disconnect_settings.destroy()
            adminpanel_settings.destroy()
            canvas.delete(welcometext)
            try:
                if kmlichange_settings:
                    kmlichange_settings.destroy()
            except:
                pass
            login()

        def changekmli():
            curs.execute("Update Accounts SET kmli = 0 WHERE nickname = ?", (nick,))
            conn.commit()
            kmlichange_settings['text'] = "You're not staying logged in anymore."


        # Show Change KMLI button only if KMLI is enabled
        curs.execute("Select * from Accounts where kmli = 1 and nickname = ?", (nick,))
        checkkmlisettings = curs.fetchone()
        if checkkmlisettings is not None:
            kmlichange_settings = Button(window, bd=2, highlightthickness=0, text="Don't stay logged in anymore",
                                         font=playfont,
                                         fg=textcolor,
                                         command=changekmli, bg=backgroundcolor, anchor="w")
            kmlichange_settings.grid(row=5, column=0, columnspan=3, sticky='EWNS')

        # Show Change KMLI button only if KMLI is enabled
        curs.execute("Select * from Accounts where admin = 1 and nickname = ?", (nick,))
        checkadminsettings = curs.fetchone()
        if checkadminsettings is not None:
            adminpanel_settings = Button(window, bd=2, highlightthickness=0, text="Admin Panel",
                                             font=playfont,
                                             fg=textcolor,
                                             command=adminuser, bg=backgroundcolor, anchor="w")
            adminpanel_settings.grid(row=4, column=2, columnspan=1, sticky='EWNS')

        # Buttons

        changepassword_settings = Button(window, bd=2, highlightthickness=0, text="Change Password", font=playfont,
                                         fg=textcolor,
                                         command=changepasswordsettings, bg=backgroundcolor, anchor="w")
        changepassword_settings.grid(row=4, column=0, columnspan=2, sticky='EWNS')

        disconnect_settings = Button(window, bd=2, highlightthickness=0, text="Disconnect", font=playfont,
                                         fg=textcolor,
                                         command=disconnectsettings, bg=backgroundcolor, anchor="w")
        disconnect_settings.grid(row=6, column=0, columnspan=2, sticky='EWNS')

        returnbutton = Button(window, bd=0, highlightthickness=0, text="Return", font=playfont, fg="white",
                              command=returnmenu, bg="orange")
        returnbutton.grid(row=1, column=0, columnspan=1, sticky='EWNS')

        colormode_settings = Button(window, bd=2, highlightthickness=0, text="Switch Dark/Light mode", font=playfont,
                                    fg=textcolor,
                                    command=switchmode, bg=backgroundcolor, anchor="w")
        colormode_settings.grid(row=2, column=0, columnspan=3, sticky='EWNS')

        version_settings = Button(window, bd=2, highlightthickness=0, text="About the console", font=playfont,
                                  fg=textcolor,
                                  command=versionsettings, bg=backgroundcolor, anchor="w")
        version_settings.grid(row=3, column=0, columnspan=3, sticky='EWNS')

        # Button to exit prog without shutting down the Rpi
        def exitprog():
            sys.exit()

        exitprog_settings = Button(window, bd=2, highlightthickness=0, text="Exit Prog", font=playfont, fg=textcolor,
                                   command=exitprog, bg=backgroundcolor, anchor="w", relief=FLAT)
        exitprog_settings.grid(row=6, column=2, columnspan=1, sticky='EWNS')

    # Setting the Button
    settingsbutton = Button(window, image=settingsDI, bd=0, highlightthickness=0, command=settings, relief=FLAT)
    settingsbutton.grid(row=2, column=1, columnspan=1, sticky='EWNS')

    def settingsbuttonhover(e):
        settingsbutton['image'] = settings_hoverDI

    def settingsbuttonunhover(e):
        settingsbutton['image'] = settingsDI

    settingsbutton.bind("<Enter>", settingsbuttonhover)
    settingsbutton.bind("<Leave>", settingsbuttonunhover)

    ### Appsbutton

    def apps():
        # Destroy all the buttons that existed
        destroymenu()

        # configure the grid
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
        title_canvas.create_text(400, 47.5, font=(playfont, 35), text="Apps", fill="white")
        title_canvas.grid(row=1, column=1, columnspan=2, sticky='EWNS')

        # Return button
        def returnmenu():
            title_canvas.destroy()
            returnbutton.destroy()
            menu(nick)

        returnbutton = Button(window, bd=0, highlightthickness=0, text="Return", font=playfont, fg="white",
                              command=returnmenu, bg="orange")
        returnbutton.grid(row=1, column=0, columnspan=1, sticky='EWNS')

    appsbutton = Button(window, image=appsDI, relief=RIDGE, bd=0, highlightthickness=0, command=apps)
    appsbutton.grid(row=1, column=2, columnspan=1, sticky='EWNS')

    def appsbuttonhover(e):
        appsbutton['image'] = apps_hoverDI

    def appsbuttonunhover(e):
        appsbutton['image'] = appsDI

    appsbutton.bind("<Enter>", appsbuttonhover)
    appsbutton.bind("<Leave>", appsbuttonunhover)


login()
window.mainloop()
