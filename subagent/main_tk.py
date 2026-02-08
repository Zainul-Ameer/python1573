import tkinter
from tkinter import ttk


# Main Window
window = tkinter.Tk()
window.title(" --Enter Subagent Details--")

# sub- window or frame
frame = tkinter.Frame(window)
frame.pack()
""" 



   1. Add New Sub Agent
   2. Check Outstanding Balance by Passport Number
   3. Sub Agent Payment for Housemaid's Passport Number
   4. Add Housemaid's Record
   5. Display Workers Name List
   6. Commission 
   7. Departure 
   8. Sub Agent Outstanding 
   9. All Sub Agents Outstanding
  10. Sub Agent Outstanding details 
  11. Print Report Housemaid
  12. Report by Date
  13. Sub Agent List
  14. Departure Housemaid Account Details
   0. Exit


one = tkinter.Label(frame, text="1. Add New Sub Agent")
one.grid(row=1, column=1)

two = tkinter.Label(frame, text="2. Display Workers Name List")
two.grid(row=2, column=1)

three = tkinter.Label(frame, text="3. Commission")
three.grid(row=3, column=1)

four = tkinter.Label(frame, text="4. Departure")
four.grid(row=4, column=1)

one = tkinter.Label(frame, text="5. Display Workers Name List")
one.grid(row=5, column=1)
"""


# Function to create labels with left alignment
def create_label(text, row):
    label = tkinter.Label(frame, text=text, anchor="w")
    label.grid(row=row, column=0, sticky="w")

# Labels
create_label("1. Add New Sub Agent", 1)
create_label("2. Display Workers Name List", 2)
create_label("3. Commission", 3)
create_label("4. Departure", 4)
create_label("5. Display Workers Name List", 5)
create_label("6. Display Workers Name List", 6)
create_label("7. Display Workers Name List", 7)
create_label("8. Display Workers Name List", 8)
create_label("9. Display Workers Name List", 9)
create_label("10. Display Workers Name List", 10)
create_label("11. Display Workers Name List", 11)
window.mainloop()


