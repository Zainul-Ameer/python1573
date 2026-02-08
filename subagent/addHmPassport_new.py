import tkinter as tk
from tkinter import messagebox
import sqlite3

def save_record():
    pp_no = entry_passport.get()
    if pp_no == "0":
        root.destroy()
        return

    cursor.execute("SELECT * FROM PassportHm WHERE PassportNo=?", (pp_no,))
    record = cursor.fetchone()

    if record:
        messagebox.showinfo("Existing Record", f"Passport Number: {record[0]}\nHousemaid's Name: {record[1]}")
    else:
        hm_name = entry_hm_name.get()
        commission = int(entry_commission.get())
        sub_id = int(entry_sub_id.get())

        cursor.execute("SELECT * FROM SubAgent WHERE sub_id=?", (sub_id,))
        sub_agent = cursor.fetchone()

        if sub_agent:
            sub_name = sub_agent[1]
            cursor.execute("INSERT INTO PassportHm (PassportNo, Name, Comm, sub_id, sub_name) VALUES (?, ?, ?, ?, ?)",
                           (pp_no, hm_name, commission, sub_id, sub_name))
            connection.commit()
            messagebox.showinfo("Record Saved", "Record saved successfully!")
        else:
            messagebox.showerror("Sub-agent not found", f"Sub-agent with ID {sub_id} not found.")

    entry_passport.delete(0, tk.END)
    entry_hm_name.delete(0, tk.END)
    entry_commission.delete(0, tk.END)
    entry_sub_id.delete(0, tk.END)

root = tk.Tk()
root.title("PassportHm Records")

# Create and place labels and entry widgets
label_passport = tk.Label(root, text="Passport Number:")
label_hm_name = tk.Label(root, text="Housemaid's Name:")
label_commission = tk.Label(root, text="Commission:")
label_sub_id = tk.Label(root, text="Sub-agent ID:")

entry_passport = tk.Entry(root)
entry_hm_name = tk.Entry(root)
entry_commission = tk.Entry(root)
entry_sub_id = tk.Entry(root)

label_passport.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
label_hm_name.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
label_commission.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
label_sub_id.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

entry_passport.grid(row=0, column=1, padx=5, pady=5)
entry_hm_name.grid(row=1, column=1, padx=5, pady=5)
entry_commission.grid(row=2, column=1, padx=5, pady=5)
entry_sub_id.grid(row=3, column=1, padx=5, pady=5)

# Create and place save button
save_button = tk.Button(root, text="Save Record", command=save_record)
save_button.grid(row=4, column=0, columnspan=2, pady=10)

# Connect to the SQLite database
connection = sqlite3.connect('SubAgentAccount.db')
cursor = connection.cursor()

root.mainloop()

# Close the database connection
connection.close()
