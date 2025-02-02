import os.path
import tkinter.filedialog
from convert import search_text_in_pdf

import ttkbootstrap as tb
from ttkbootstrap.constants import *

OUTPUTS_IMG = 'D:/Descargas/Horarios'

# root
root = tb.Window(themename='darkly')
root.geometry('500x290')
root.iconbitmap('pdf-icon.ico')

# styles
Style = tb.Style()
Style.configure('TLabel', font=('Segoe UI', 14, 'bold'))
Style.configure('TButton', font=('Segoe UI', 10))

# Title
title_lbl = tb.Label(text='PDF Converter')
title_lbl.pack(pady=30)
pdf_frame = tb.Frame(root)
pdf_frame.pack(pady=10)

# Functions
def search_filename():
    filename = tkinter.filedialog.askopenfilename()
    if filename:
        pdf_path_entry.insert(END,filename)
    else:
        title_lbl.configure(text='Please select a valid file')

def convert_file():
    filepath = pdf_path_entry.get()
    if filepath:

        search_text_in_pdf(filepath)
    else:
        title_lbl.configure(text='Invalid filepath')

def open_folder():
    path = os.path.realpath(OUTPUTS_IMG)
    os.startfile(path)


# Widgets
pdf_path_entry = tb.Entry(pdf_frame, style='info', width=70)
pdf_path_entry.grid(row=0, column=0, columnspan=2, pady=10)

search_btn = tb.Button(pdf_frame, text='Search file', width=20, command=search_filename)
search_btn.grid(row=1, column=0)
convert_btn = tb.Button(pdf_frame, text='Convert pdf', width=20, style='outline-info', command=convert_file)
convert_btn.grid(row=1, column=1)


pdf_img_var = tb.StringVar(value=OUTPUTS_IMG)
pdf_img_entry = tb.Entry(root, textvariable=pdf_img_var, width=70, state=READONLY)
pdf_img_entry.pack(padx=10, pady=5)

folder_btn = tb.Button(root, text='Open folder', width=20, style='outline-info', command=open_folder)
folder_btn.pack()


root.mainloop()
