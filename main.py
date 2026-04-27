import customtkinter as ctk
from tkinter import filedialog
from images import convert_image

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

app = ctk.CTk()
app.title("File Converter")
app.geometry("600x400")

selected_file = ctk.StringVar()

tabview = ctk.CTkTabview(app)
tabview.pack(fill="both", expand=True, padx=20, pady=20)

tabview.add("Images")
tabview.add("Documents")
tabview.add("Audio")
tabview.add("Video")

images_tab = tabview.tab("Images")

btn_choose = ctk.CTkButton(images_tab, text="Choose file", command=choose_file)
btn_choose.pack(pady=20)

label_file = ctk.CTkLabel(images_tab, text="No file selected", wraplength=500)
label_file.pack(pady=5)

format_var = ctk.StringVar(value="png")
dropdown = ctk.CTkOptionMenu(images_tab, values=["jpg", "png", "webp", "bmp", "tiff", "gif", "ico", "avif"], variable=format_var)
dropdown.pack(pady=10)

btn_convert = ctk.CTkButton(images_tab, text="Convert", command=convert)
btn_convert.pack(pady=10)

app.mainloop()