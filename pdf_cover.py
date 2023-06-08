import os
from pypdf import PdfMerger, PdfReader, PdfWriter

'''This tool is used to remove the front page from a specified PDF and append it to all PDFs in a specified directory'''

cover = input("Drag and drop the cover file, and remove qoutes\n")
folder = input(
    "Drag and drop the source folder, remove qoutes, and add a backslash\n")

# Ensure the folder path is a folder path.
is_folder = folder[len(folder) - 1]
if is_folder != "\\":
    print("Please close your folder!")
    quit()

# Create a tempory cover page from the existing document.
reader = PdfReader(cover)
cover_page = reader.pages[0]
output = PdfWriter()
output.add_page(cover_page)
output.write("cover_page.pdf")

# Iterate through the merge directory.
for filename in os.listdir(folder):
    merger = PdfMerger()
    doc_2 = folder + filename
    merge = ["cover_page.pdf", doc_2]
    for sheet in merge:
        merger.append(sheet)

    merger.write(doc_2)
    merger.close()

# Delete the temporary cover page.
os.remove("cover_page.pdf")
