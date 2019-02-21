#imports
from tkinter import *
from tkinter import font
import random, os, time, sys
from PIL import ImageTk


window = Tk()
window.title('3P!U The Updater')

### Window size
# Uncomment this one for a rasp install
window.attributes('-fullscreen', True)
# Uncomment this one for a windows install
#window.geometry("1200x600")