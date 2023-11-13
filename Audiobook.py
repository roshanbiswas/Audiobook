# imports
import PyPDF2
import pyttsx3
import os
import time


def extract_from_pdf(file_path: str):
    """Function to extract text from a PDF file

    Args:
        file_path (str): path to file containing text.

    Returns:
        txt: text from audiobook file
    """
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(0, len(pdf_reader.pages)):
            text += pdf_reader.pages[page].extract_text()
    return text


def extract_from_txt(file_path: str):
    """Function to extract text from a TXT file

    Args:
        file_path (str): path to file containing text.

    Returns:
        txt: text from audiobook file
    """
    with open(file_path, "r") as file:
        return file.read()


def extract_text(file_path: str):
    """function to detect file type and extract text accordingly

    Args:
        file_path (str): path to file containing text.

    Returns:
        txt: text from audiobook file
    """
    _, file_extension = os.path.splitext(file_path)
    if file_extension == ".pdf":
        return extract_from_pdf(file_path)
    elif file_extension == ".txt":
        return extract_from_txt(file_path)
    else:
        return "Unsupported file type."


def convert_text_to_speech(text: str, rate: int = 250):
    """function that uses pyttsx3 to convert text to speech

    Args:
        text (str): text which is converted to speech
        rate (int, optional): rate of speech. Defaults to 250.
    """
    # Initialize the speech engine
    speak = pyttsx3.init()
    speak.setProperty("rate", rate)
    speak.say(text)
    speak.runAndWait()


def user_interaction():
    """takes all needed inputs and calls extract_text() and convert_text_to_speech()"""
    # Get file path from user
    file_path = input("Please enter the path to your file: ")

    # Extract and Convert text
    text = extract_text(file_path)
    convert_text_to_speech(text)


if __name__ == "__main__":
    user_interaction()
