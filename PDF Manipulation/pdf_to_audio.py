## This code is a Python script that reads a PDF file, converts the text 
## from the PDF file into speech using text-to-speech (TTS) technology, 
## and saves the resulting audio file. 

# imports
from PyPDF2 import PdfReader
import pyttsx3

# read in the pdf, will need to change if multiple pdfs
pdf_reader = PdfReader('INSERT FILE PATH HERE')
# This line initializes the TTS engine and assigns it to the variable speaker.
speaker = pyttsx3.init()


# This loop iterates through each page of the PDF file and extracts the text 
# from the page using the extract_text() method. The extracted text is then 
# cleaned by removing leading and trailing whitespace and replacing line breaks 
# with empty strings. Finally, the cleaned text is printed to the console.
for page_num in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[page_num].extract_text(0)
    clean_text = text.strip().replace('\n', '')
    print(clean_text)

# This code block converts the cleaned text into an audio file named story.mp3 
# using the save_to_file() method. The TTS engine then runs the conversion and 
# plays the audio file using runAndWait(). Finally, the TTS engine is stopped 
# using stop().
speaker.save_to_file(clean_text,'story.mp3')
speaker.runAndWait()
speaker.stop()