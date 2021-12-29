from tkinter import *
from PIL import Image, ImageTk
from time import strftime
import datetime




root = Tk()
root.title("Date and Time")
icon = PhotoImage(file='icons8-time-50.png')
root.iconphoto(False, icon)




today = datetime.datetime.now()

def date():
    d = today.strftime('%d %B %Y')
    label1.config(text = d)


def time():
    strng = strftime('%I:%M:%S %p')
    label2.config(text = strng)
    label2.after(1000,time)

label1 = Label(root,font = ("Sanserif",16,"bold","italic"), background = 'black', foreground = 'orange', width = 30, padx = 5, pady = 5)
label1.pack(anchor = 'center')
date()

label2 = Label(root, font = ("Courier",16,"bold"),background = 'black', foreground = 'cyan', width = 30, padx = 5, pady = 5)
label2.pack(anchor = 'center')
time()


mainloop()