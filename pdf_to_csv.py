from pypdf import PdfReader
import tabula as tb
import csv

'''This tool is used to extract tables from PDF documents'''

# Request source PDF and output directory
pdf_file = input("Drag and drop the pdf file, and remove qoutes\n")
dest_folder = input(
    "Drag and drop the destination folder, and add a backslash\n")

# Ensure the folder path is a folder path.
is_folder = dest_folder[len(dest_folder) - 1]
if is_folder != "\\":
    print("Please close your folder!")
    quit()

# Rename the .pdf to .csv
csv_file = pdf_file[:-3] + "csv"

# Get a page count for iterable range
reader = PdfReader(pdf_file)
page_count = len(reader.pages)

# Create a csv file to write/apend to
with open(csv_file, 'w') as file:
    writer = csv.writer(file)

# Extract all tables from the PDF.
if page_count == 2:
    out_file = tb.read_pdf(pdf_file, pages=2)[0]
    out_file.to_csv(csv_file)
else:
    for page in range(2, page_count + 1):
        out_file = tb.read_pdf(pdf_file, pages=page)[0]
        out_file.to_csv(csv_file, mode='a')