import pyperclip
import pyshorteners
from tkinter import *

#Writing the function for shortening
def shortener():
    long_url=url.get()
    short_url=pyshorteners.Shortener().tinyurl.short(long_url)
    url_shortener.set(short_url)
def copyurl():
    url_c=url_shortener.get()
    pyperclip.copy(url_c)

window=Tk()
window.geometry("200x200")
window.title("Url Shortener")
window.config(bg='cyan')
#Url variables as string
url=StringVar()
url_shortener=StringVar()

#Designing the GUI
Label(window,text='Enter the Url',font='roboto').pack(pady=5)
Entry(window,textvariable=url).pack(pady=3)
Button(window,text='Shorten it!',command=shortener).pack(pady=5)
Label(window,text='Shortened Url',font='roboto').pack(pady=5)
Entry(window,textvariable=url_shortener).pack(pady=4)
Button(window,text='Copy it!',command=copyurl).pack(pady=4)

window.mainloop()
