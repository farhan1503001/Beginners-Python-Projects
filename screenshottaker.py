import pyautogui
from tkinter.filedialog import *
import tkinter as tk
#Initialize the window
def take_screenshot():
    screenshot=pyautogui.screenshot() #Taking the screenshot
    directory=asksaveasfilename() #Open for a file directory
    screenshot.save(directory+'screenshot.png')

window=tk.Tk()
#Now initializing a canvas and setting the window there.
canvas1=tk.Canvas(window,width=300,height=300)
canvas1.pack() #Now packing the whole canvas
#Creating the button
presser=tk.Button(text='Take Screenshot',command=take_screenshot,font=14)
#Now creating the whole window with canvas
canvas1.create_window(160,160,window=presser)

window.mainloop()