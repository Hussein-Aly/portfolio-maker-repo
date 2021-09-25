from docx2pdf import convert
import os
from PIL import Image
from fpdf import FPDF

# Configure API key authorization: Apikey


def word_to_pdf(input_file):
    convert(input_file)
    os.remove(input_file)


def img_to_pdf(input_file):
    img = Image.open(input_file)
    img = img.convert('RGB')
    img.save(input_file.rsplit(".", 1)[0] + '.pdf')
    os.remove(input_file)


def txt_to_pdf(input_file):

    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=15)

    # open the text file in read mode
    f = open(input_file, "r")

    # insert the texts in pdf
    for x in f:
        pdf.cell(200, 10, txt=x, ln=1, align='C')

    # save the pdf with name .pdf
    f.close()
    pdf.output(input_file.rsplit(".", 1)[0] + '.pdf')
    os.remove(input_file)


def convert_to_pdf(input_files):
    for input_file in input_files:
        try:
            print(input_file)
            if input_file.endswith('docx') or input_file.endswith('doc'):
                word_to_pdf(input_file)
            elif input_file.endswith('png') or input_file.endswith('jpg'):
                img_to_pdf(input_file)
            elif input_file.endswith('txt'):
                txt_to_pdf(input_file)

        except IOError:
            print("file doesn't end with: docx, doc, png or jpg!")
