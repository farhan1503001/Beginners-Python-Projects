from tkinter import *
from tkinter.ttk import *
from time import strftime

#Now initializing the window
window=Tk()
window.title("Digital Clock")

def time():
    time_value=strftime('%H:%M:%S %p')#Format for converting time to string
    label.config(text=time_value)#Setting the label with string value
    label.after(1000,time)

label=Label(window,font=("ds-digital",80), background='black',foreground='cyan')#Setting the window inside the label
label.pack(anchor='center')#Setting the label at the center
time()
mainloop()