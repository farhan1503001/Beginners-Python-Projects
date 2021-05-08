from tkinter import *
from tkinter import colorchooser
#Initializing the window
def click():
    color=colorchooser.askcolor()
    print(color)
    colorhexa=color[1]
    window.config(background=colorhexa)


window=Tk()
window.geometry("200x300") #Setting the size of the window
window.title("Color Chooser")
button=Button(text="Press Here",command=click)
button.pack()
#Displaying the loop
window.mainloop()