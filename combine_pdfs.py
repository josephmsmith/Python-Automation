# Use this script to combine multiple pdfs

# First create a venv and install PyPDF2
import os
from PyPDF2 import PdfWriter

# Create user inputs for file paths
num_pdfs = int(input("How many PDF files do you want to merge? "))
pdf_list = [input(f"What is the file path of PDF #{i+1}? ") for i in range(num_pdfs)]
new_pdf_name = input("What would you like the new file to be named(without.pdf): ")
output_directory = input("Where would you like to save the file? Insert file path: ")

# Nav to user input path
os.chdir(output_directory.strip('"'))

# Combine pdfs
with PdfWriter() as merger:
    for pdf in pdf_list:
        pdf = pdf.strip('"')
        merger.append(pdf)
    merger.write(f'{new_pdf_name}.pdf')
merger.close()

print('Done!')