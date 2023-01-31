from tkinter import *
from tkinter import colorchooser


oyna = Tk()
oyna.geometry('400x400')

def color():
    mycolor = colorchooser.askcolor()[1]
    label = Label(oyna, text = mycolor)
    label.pack(pady = 10)

button = Button(oyna, text = 'choose color', command = color)
button.pack(pady = 10)

oyna.mainloop()