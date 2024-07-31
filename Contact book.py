import tkinter as tk
from tkinter import messagebox

# Function to add a contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        contact_listbox.insert(tk.END, f"{name} - {phone}")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Both name and phone number are required.")

# Function to delete a selected contact
def delete_contact():
    try:
        selected_index = contact_listbox.curselection()[0]
        contact_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a contact to delete.")

# Create the main application window
root = tk.Tk()
root.title("Simple Contact Book")

# Create and place widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

name_label = tk.Label(frame, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)

name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

phone_label = tk.Label(frame, text="Phone Number:")
phone_label.grid(row=1, column=0, padx=5, pady=5)

phone_entry = tk.Entry(frame, width=30)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

add_button = tk.Button(frame, text="Add Contact", command=add_contact)
add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

contact_listbox = tk.Listbox(frame, width=50, height=10)
contact_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

delete_button = tk.Button(frame, text="Delete Contact", command=delete_contact)
delete_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()
