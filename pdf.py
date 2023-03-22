import PyPDF2

with open('dummyfiles/dummy.pdf', 'rb') as file: # 'rb': means read binary
    # print(file)
    reader = PyPDF2.PdfReader(file)
    print(len(reader.pages))
    page = reader.pages[0]
    page.rotate(-90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open('dummyfiles/tilt.pdf', 'wb') as new_file:
        writer.write(new_file)