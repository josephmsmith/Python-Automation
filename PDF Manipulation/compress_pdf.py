# use this code to compress pdfs
# install PyPDF2 first!!

from PyPDF2 import PdfReader, PdfWriter

pdf_path = input("What is the file path to the pdf? ").strip('"')
new_pdf_name = input("What do you want your compressed pdf to be called?(add .pdf) ")

reader = PdfReader(pdf_path)
writer = PdfWriter()

for page in reader.pages:
    page.compress_content_streams()  # This is CPU intensive!
    writer.add_page(page)

with open(new_pdf_name, "wb") as f:
    writer.write(f)