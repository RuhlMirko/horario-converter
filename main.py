import os.path
import tkinter.filedialog
from convert import search_text_in_pdf

import ttkbootstrap as tb
from ttkbootstrap.constants import *

OUTPUTS_IMG = 'D:/Descargas/Horarios'

# root
root = tb.Window(themename='darkly')
root.iconbitmap('pdf-icon.ico')

# Center app on window
app_width = 500
app_height = 290
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width/2) -(app_width/2))
y = int((screen_height/2) -(app_height/2))

root.geometry(f'{app_width}x{app_height}+{x}+{y}')


# styles
Style = tb.Style()
Style.configure('titleLabel.TLabel', font=('Segoe UI', 14, 'bold'))
Style.configure('path.TLabel', font=('Segoe UI', 10, 'italic'), foreground='#666')
Style.configure('TButton', font=('Segoe UI', 10))

# Title
title_lbl = tb.Label(text='PDF Converter', style='titleLabel.TLabel')
title_lbl.pack(pady=30)
pdf_frame = tb.Frame(root)
pdf_frame.pack(pady=10)

# Functions
def search_filename():
    pdf_path_entry.delete(0, END)
    filename = tkinter.filedialog.askopenfilename()
    if filename:
        pdf_path_entry.insert(END, filename)
    else:
        title_lbl.configure(text='Please select a valid file', bootstyle='danger')

def convert_file():
    filepath = pdf_path_entry.get()
    if filepath.endswith('.pdf'):
        pdf_path_entry.delete(0, END)
        title_lbl.configure(text='Image ready on folder', bootstyle='success')
        search_text_in_pdf(filepath)
    else:
        title_lbl.configure(text='Invalid filepath', bootstyle='danger')


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


pdf_lbl_path = tb.Label(root, text=OUTPUTS_IMG, style='path.TLabel')
pdf_lbl_path.pack(padx=10, pady=5)

folder_btn = tb.Button(root, text='Open folder', width=20, style='outline-info', command=open_folder)
folder_btn.pack()


root.mainloop()
