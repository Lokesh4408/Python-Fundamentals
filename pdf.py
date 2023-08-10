import PyPDF2
# import sys

# inputs = sys.argv[1:]

# with open('dummyfiles/dummy.pdf', 'rb') as file: # 'rb': means read binary
#     # print(file)
#     reader = PyPDF2.PdfReader(file)
#     print(len(reader.pages))
#     page = reader.pages[0]
#     page.rotate(-90)
#     writer = PyPDF2.PdfWriter()
#     writer.add_page(page)
#     with open('dummyfiles/tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)

# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('dummyfiles/combined.pdf')
        
# pdf_combiner(inputs)

# with open('dummyfiles/combined.pdf', 'wb') as wtr_file:
# merger1 = PyPDF2.PdfMerger()
# merger1.append('dummyfiles/combined.pdf')
# merger1.append('dummyfiles/wtr.pdf')
# merger1.write('dummyfiles/wtr_combined.pdf')


# -----Watermark all the pages of the combined pdf document-----
template = PyPDF2.PdfReader(open('dummyfiles/combined.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('dummyfiles/wtr.pdf', 'rb'))
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template._get_page(i)
    page.merge_page(watermark._get_page(0))
    output.add_page(page)
    
    with open('dummyfiles/watermarked_output.pdf', 'wb') as file:
        output.write(file)
