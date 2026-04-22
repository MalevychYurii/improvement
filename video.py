import ffmpeg
import os

supported_formats = ["mp4", "avi", "mkv", "mov", "webm"]

def convert_video(input_path, output_format):
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return

    input_format = os.path.splitext(input_path)[1].replace(".", "")

    if input_format not in supported_formats:
        print(f"Unsupported format: {input_format}")
        print(f"Supported formats: {', '.join(supported_formats)}")
        return

    if input_format == output_format:
        print("The input and output formats are the same - no conversion is needed")
        return

    name = os.path.splitext(input_path)[0]
    output_path = f"{name}.{output_format}"

    ffmpeg.input(input_path).output(output_path).run()
    print(f"Saved as: {output_path}")

convert_video("test.mp4", "avi")