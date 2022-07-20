from tkinter import *
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
import urllib
from urllib import request
from datetime import datetime
from requests import get


oyna = Tk()
oyna.title('Bitcoin Price Grabber')
oyna.iconphoto(False, PhotoImage(file = 'learning.png'))
oyna.resizable(False, False)
oyna.geometry('550x210')
oyna.config(bg = 'black')

global previous 
previous = False

now = datetime.now()
current_time = now.strftime("%I:%M:%S %p")



my_frame = Frame(oyna, bg = 'black')
my_frame.pack(pady= 20)

logo = ImageTk.PhotoImage(Image.open('icons/bitcoin.png').resize((80,80), Image.ANTIALIAS))
logo_label = Label(my_frame, image = logo, bd = 0, bg = 'green')
logo_label.grid(row = 0 ,column= 0, rowspan = 2)

bit_label = Label(my_frame, text = 'TEST', font = ("Helvetica", 45), bg = 'black', fg = 'green', bd = 0)
bit_label.grid(row = 0, column= 1, padx = 20, sticky='s')

latest_label = Label(my_frame, text = 'MOVE TEST', font = ("Helvetica", 8), bg = 'black', fg = 'green', bd = 0)
latest_label.grid(row = 1, column = 1, sticky= 'n')


def Update():
    global previous
   
    page = urllib.request.urlopen("https://www.coindesk.com/price/bitcoin").read()
    html = BeautifulSoup(page, 'html.parser')
    price_large = html.find(class_="price-large")
    
    print(price_large)
    
    price_large1 = str(price_large)
    
    price_large2 = price_large1[54:63]
    
    bit_label.config(text = f"price_large2")
    
    

    
    oyna.after(30000, Update)
    
    
status_bar = Label(oyna, text = f'Last Updated{current_time}   ', bd = 0, anchor=E, bg = 'black', fg = 'grey')
status_bar.pack(fill = X, side = BOTTOM, ipady = 2)

    
    






Update()
oyna.mainloop() 