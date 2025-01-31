import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename='darkly')
root.geometry('500x400')

pdf_frame = ttk.Frame(root, relief='sunken')
pdf_frame.pack(pady=50)

pdf_path_entry = ttk.Entry(pdf_frame, style='info', width=70)
pdf_path_entry.pack()

root.mainloop()
