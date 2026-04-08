from docx2pdf import convert
from pdf2docx import Converter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

supported_input_formats = ["docx", "pdf", "txt"]

def convert_document(input_path, output_format):
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return

    input_format = os.path.splitext(input_path)[1].replace(".", "") # витягує формат
    name = os.path.splitext(input_path)[0]
    output_path = f"{name}.{output_format}"

    if input_format not in supported_input_formats:
        print(f"Unsupported format: {input_format}")
        print(f"Supported formats: {', '.join(supported_input_formats)}")
        return

    if input_format == "docx" and output_format == "pdf":
        convert(input_path, output_path)
    elif input_format == "pdf" and output_format == "docx":
        cv = Converter(input_path)
        cv.convert(output_path)
        cv.close()
    elif input_format == "txt" and output_format == "pdf":
        txt_to_pdf(input_path, output_path)
    else:
        print(f"Conversion from {input_format} to {output_format} is not supported")
        return

    print(f"Saved as: {output_path}")


def txt_to_pdf(input_path, output_path):
    pdf = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    y = height - 50

    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            if y < 50:
                pdf.showPage()
                y = height - 50
            pdf.drawString(50, y, line.strip())
            y -= 20

    pdf.save()

convert_document("test.txt", "pdf")