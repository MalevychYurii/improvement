from docx2pdf import convert
import os

def convert_document(input_path, output_format):
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return

    name = os.path.splitext(input_path)[0]
    output_path = f"{name}.{output_format}"

    convert(input_path, output_path)
    print(f"Saved as: {output_path}")

convert_document("test.docx", "pdf")