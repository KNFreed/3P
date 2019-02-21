#imports
import git
from tkinter import *

window = Tk()
window.title('3P!U The Updater')

### Window size
# Uncomment this one for a rasp install
#window.attributes('-fullscreen', True)
# Uncomment this one for a windows install
window.geometry("1200x600")

repo = git.Repo('./')
update = repo.remotes.origin
update.pull()
