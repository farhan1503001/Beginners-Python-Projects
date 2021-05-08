import pyttsx3
import PyPDF2
from tkinter.filedialog import *
#Ask for book file 
book_file=askopenfilename()
pdfreader=PyPDF2.PdfFileReader(book_file)#Initialize Reading the pdf file
num_pages=pdfreader.numPages#Finds the number of pages in that book
#Now iterate through each and every page and convert that to audio
for page in range(num_pages):
    book_page=pdfreader.getPage(page)
    #Now extract the text from book's page
    text=book_page.extractText()
    #Initialize the text to speech object
    text_to_speech=pyttsx3.init()
    #starts speaking the text from the object
    text_to_speech.say(text)
    text_to_speech.runAndWait()