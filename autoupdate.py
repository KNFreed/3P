#imports
import git, time
from tkinter import *
from PIL import ImageTk

window = Tk()
window.title('3P!U The Updater')

### Window size
# Uncomment this one for a rasp install
#window.attributes('-fullscreen', True)
# Uncomment this one for a windows install
window.geometry("1200x600")

backgroundImage = ImageTk.PhotoImage(file="./files/updating.png")
background_label = Label(window, image=backgroundImage)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def update():
    repo = git.Repo('./')
    update = repo.remotes.origin
    update.pull()
    exec(open('Ui.py').read())
    time.sleep(2)
    window.destroy
time.sleep(2)
update()
mainloop()