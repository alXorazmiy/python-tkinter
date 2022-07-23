from tkinter import *
from PIL import ImageTk, Image

def select_all():
    for check in [over_18,over_17,fallow]:
        check.select()


def deselect_all():
    for check in [over_18,over_17,fallow]:
        check.deselect()
        

def switch_all():
    for check in [over_18,over_17,fallow]:
        check.toggle()

def show ():
    print('siz 18 yoshsiz', over_18_value.get())

oyna = Tk()  
oyna.title('calculator')
oyna.geometry('400x500+800+100')
oyna.config(bg = '#6ACBDE')

over_18_value = StringVar()
over_18_value.set('No ')
over_17_value = IntVar()

img = ImageTk.PhotoImage(Image.open('icons/info.png').resize((10,10), Image.ANTIALIAS))

over_18 = Checkbutton(oyna, text = 'siz 18 yoshmisiz',
                      variable = over_18_value,
                      offvalue = 'No',
                      onvalue = "Yes",
                      image = img
                      )
over_18.pack()
over_17 = Checkbutton(oyna, text= 'siz 17 yoshmisiz')
over_17.pack()
fallow = Checkbutton(oyna, text = 'saytga obuna boling', indicatoron = 0, bg = 'red')
fallow.pack()
Button(oyna, text = 'show', command = show).pack()


Button (oyna, text = 'select_all', command = select_all).pack()
Button (oyna, text = 'deselect_all', command = deselect_all).pack()
Button (oyna, text = 'switch_all', command = switch_all).pack()

oyna.mainloop()