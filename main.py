import customtkinter as ctk
from tkinter import filedialog
from images import convert_image
from documents import convert_document
from audio import convert_audio
from video import convert_video

app = ctk.CTk()
app.title("File Converter")
app.geometry("600x400")

tabview = ctk.CTkTabview(app)
tabview.pack(fill="both", expand=True, padx=20, pady=20)

tabview.add("Images")
tabview.add("Documents")
tabview.add("Audio")
tabview.add("Video")

def setup_images_tab():
    tab = tabview.tab("Images")
    selected_file = ctk.StringVar()

    def choose_file():
        path = filedialog.askopenfilename()
        if path:
            selected_file.set(path)
            label_file.configure(text=path)

    def convert():
        path = selected_file.get()
        fmt = format_var.get()
        if path:
            convert_image(path, fmt)
        else:
            print("No file selected")

    btn_choose = ctk.CTkButton(tab, text="Choose file", command=choose_file)
    btn_choose.pack(pady=20)

    label_file = ctk.CTkLabel(tab, text="No file selected", wraplength=500)
    label_file.pack(pady=5)

    format_var = ctk.StringVar(value="png")
    dropdown = ctk.CTkOptionMenu(tab, values=["jpg", "png", "webp", "bmp", "tiff", "gif", "ico", "avif"], variable=format_var)
    dropdown.pack(pady=10)

    btn_convert = ctk.CTkButton(tab, text="Convert", command=convert)
    btn_convert.pack(pady=10)

def setup_documents_tab():
    tab = tabview.tab("Documents")
    selected_file = ctk.StringVar()

    def choose_file():
        path = filedialog.askopenfilename()
        if path:
            selected_file.set(path)
            label_file.configure(text=path)

    def convert():
        path = selected_file.get()
        fmt = format_var.get()
        if path:
            convert_document(path, fmt)
        else:
            print("No file selected")

    btn_choose = ctk.CTkButton(tab, text="Choose file", command=choose_file)
    btn_choose.pack(pady=20)

    label_file = ctk.CTkLabel(tab, text="No file selected", wraplength=500)
    label_file.pack(pady=5)

    format_var = ctk.StringVar(value="pdf")
    dropdown = ctk.CTkOptionMenu(tab, values=["pdf", "docx"], variable=format_var)
    dropdown.pack(pady=10)

    btn_convert = ctk.CTkButton(tab, text="Convert", command=convert)
    btn_convert.pack(pady=10)

def setup_audio_tab():
    tab = tabview.tab("Audio")
    selected_file = ctk.StringVar()

    def choose_file():
        path = filedialog.askopenfilename()
        if path:
            selected_file.set(path)
            label_file.configure(text=path)

    def convert():
        path = selected_file.get()
        fmt = format_var.get()
        if path:
            convert_audio(path, fmt)
        else:
            print("No file selected")

    btn_choose = ctk.CTkButton(tab, text="Choose file", command=choose_file)
    btn_choose.pack(pady=20)

    label_file = ctk.CTkLabel(tab, text="No file selected", wraplength=500)
    label_file.pack(pady=5)

    format_var = ctk.StringVar(value="mp3")
    dropdown = ctk.CTkOptionMenu(tab, values=["mp3", "wav", "flac", "ogg", "aac"], variable=format_var)
    dropdown.pack(pady=10)

    btn_convert = ctk.CTkButton(tab, text="Convert", command=convert)
    btn_convert.pack(pady=10)

def setup_video_tab():
    tab = tabview.tab("Video")
    selected_file = ctk.StringVar()

    def choose_file():
        path = filedialog.askopenfilename()
        if path:
            selected_file.set(path)
            label_file.configure(text=path)

    def convert():
        path = selected_file.get()
        fmt = format_var.get()
        if path:
            convert_video(path, fmt)
        else:
            print("No file selected")

    btn_choose = ctk.CTkButton(tab, text="Choose file", command=choose_file)
    btn_choose.pack(pady=20)

    label_file = ctk.CTkLabel(tab, text="No file selected", wraplength=500)
    label_file.pack(pady=5)

    format_var = ctk.StringVar(value="mp4")
    dropdown = ctk.CTkOptionMenu(tab, values=["mp4", "avi", "mkv", "mov", "webm"], variable=format_var)
    dropdown.pack(pady=10)

    btn_convert = ctk.CTkButton(tab, text="Convert", command=convert)
    btn_convert.pack(pady=10)

setup_images_tab()
setup_documents_tab()
setup_audio_tab()
setup_video_tab()

app.mainloop()