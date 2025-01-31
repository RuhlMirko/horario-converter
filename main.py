import ttkbootstrap as tb
from ttkbootstrap.constants import *
# root
root = tb.Window(themename='darkly')
root.geometry('500x400')

# styles
Style = tb.Style()
Style.configure('TLabel', font=('Segoe UI', 14, 'bold'))
Style.configure('TButton', font=('Segoe UI', 10))

# Title
title_lbl = tb.Label(text='PDF Converter')
title_lbl.pack(pady=30)
pdf_frame = tb.Frame(root)
pdf_frame.pack(pady=10)

# Widgets
pdf_path_entry = tb.Entry(pdf_frame, style='info', width=70)
pdf_path_entry.grid(row=0, column=0, columnspan=2, pady=10)

search_btn = tb.Button(pdf_frame, text='Search file', width=20)
search_btn.grid(row=1, column=0)
convert_btn = tb.Button(pdf_frame, text='Convert pdf', width=20, style='outline-info')
convert_btn.grid(row=1, column=1)




root.mainloop()
