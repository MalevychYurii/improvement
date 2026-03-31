from PIL import Image 

def convert_image(input_path, output_path):
    image = Image.open(input_path)
    image.save(output_path)

convert_image("test.jpg", "test.png")