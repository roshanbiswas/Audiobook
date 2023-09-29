# imports
import PyPDF2
import pyttsx3

path = open('script.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(path)

# the page with which you want to start
from_page = pdfReader.pages[1]

text = from_page.extract_text()

speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()