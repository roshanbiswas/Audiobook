# imports
import PyPDF2
import pyttsx3
import os
import time

# Function to extract text from a PDF file
def extract_from_pdf(file_path, start_page=0):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(start_page, len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

# Function to extract text from a TXT file
def extract_from_txt(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Main function to detect file type and extract text accordingly
def extract_text(file_path, start_page=0):
    _, file_extension = os.path.splitext(file_path)
    if file_extension == ".pdf":
        return extract_from_pdf(file_path, start_page)
    elif file_extension == ".txt":
        return extract_from_txt(file_path)
    else:
        return "Unsupported file type."

def convert_text_to_speech(text, rate=350):
    # Initialize the speech engine
    speak = pyttsx3.init()
    speak.setProperty('rate', rate)
    speak.say(text)
    speak.runAndWait()

def user_interaction():
    # Get file path from user
    file_path = input("Please enter the path to your file: ")

    # Detect file type
    _, file_extension = os.path.splitext(file_path)

    # If PDF, ask for a starting page
    start_page = 0
    if file_extension == ".pdf":
        try:
            start_page = int(input("Enter the page number to start reading from (default is 0): "))
        except ValueError:
            print("Invalid input. Starting from the first page.")
    
    # Extract and Convert text
    text = extract_text(file_path, start_page)
    convert_text_to_speech(text)
    
user_interaction()
