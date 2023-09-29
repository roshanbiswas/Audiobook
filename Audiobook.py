# imports
import PyPDF2
import pyttsx3
import time

path = open('script.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(path)

# the page with which you want to start
from_page = pdfReader.pages[1]

text = from_page.extract_text()
rate = 300
speak = pyttsx3.init()
speak.setProperty('rate', rate)
speak.say(text)
speak.runAndWait()