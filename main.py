from PIL import Image
import os

supported_formats = ["jpg", "jpeg", "png", "webp", "bmp", "tiff", "gif", "ico", "avif"]

def convert_image(input_path, output_format):
    if not os.path.exists(input_path): 
        print(f"File not found: {input_path}")
        return

    if output_format not in supported_formats:
        print(f"Unsupported format: {output_format}")
        print(f"Suppurted formats: {', '.join(supported_formats)}")
        return

    input_format = os.path.splitext(input_path)[1].replace(".", "")

    if input_format == output_format:
        print("The input and output formats are the same - no conversion is needed")
        return

    name = os.path.splitext(input_path)[0] # test.jpg
    output_path = f"{name}.{output_format}" # ('test', '.jpg')
    image = Image.open(input_path)
    image.save(output_path)
    print(f"Saved as: {output_path}")

convert_image("test.png", "jpg")