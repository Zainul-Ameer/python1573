import tkinter
from tkinter import ttk
import os

# Main Window
window = tkinter.Tk()
window.title(" --Enter Subagent Details--")

# sub- window or frame
frame = tkinter.Frame(window)
frame.pack()


subagent_info_frame = tkinter.LabelFrame(frame, text="Sub Agent Information...")
subagent_info_frame.grid(row=0, column=0, padx=20, pady=20)


subagent_id_label = tkinter.Label(subagent_info_frame, text="Eenter Subagent Id No.:")
subagent_id_label.grid(row=5, column=3)

subagent_name_label = tkinter.Label(subagent_info_frame, text="Eenter Subagent Name:")
subagent_name_label.grid(row=10, column=3)


subagent_id_entry = tkinter.Entry(subagent_info_frame)
subagent_id_entry.grid(row=5, column=4)
id = subagent_id_entry.get()

subagent_name_entry = tkinter.Entry(subagent_info_frame)
subagent_name_entry.grid(row=10, column=4)
print(f"Sub Agent Id is {id}")
window.mainloop()

print(f"Sub Agent Id is {id}")

