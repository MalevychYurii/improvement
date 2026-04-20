from pydub import AudioSegment
import os

supported_formats = ["mp3", "wav", "flac", "ogg", "aac"]

def convert_audio(input_path, output_format):
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return

    input_format = os.path.splitext(input_path)[1].replace(".", "")

    if input_format not in supported_formats:
        print(f"Unsupported format: {input_format}")
        print(f"Supported formats: {', '.join(supported_formats)}")
        return

    if input_format == output_format:
        print("Вхідний і вихідний формат однакові — конвертація не потрібна")
        return

    name = os.path.splitext(input_path)[0]
    output_path = f"{name}.{output_format}"

    audio = AudioSegment.from_file(input_path, format=input_format)
    audio.export(output_path, format=output_format)
    print(f"Saved as: {output_path}")

convert_audio("test.mp3", "wav")