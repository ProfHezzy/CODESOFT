import tkinter as tk
from tkinter import messagebox
import csv
import os

# File to store contact data
CONTACTS_FILE = "contacts.csv"

# Function to load contacts from CSV
def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            contacts = list(reader)
    return contacts

# Function to save contacts to CSV
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

# Function to add a contact
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if not name or not phone:
        messagebox.showerror("Error", "Name and Phone Number are required!")
        return
    # Chech if email is valid
    if email:
        if "@" not in email or "." not in email:
            messagebox.showerror("Error", "Invalid Email Address!")
            return
        
    # Check if phone number is valid
    if not phone.isdigit() or len(phone) < 10:
        messagebox.showerror("Error", "Invalid Phone Number!")
        return
        
    # Check if contact already exists
    for contact in load_contacts():
        if name == contact[0] or phone == contact[1]:
            messagebox.showwarning("Warning", "Contact already exists!")
            return

    contacts = load_contacts()
    contacts.append([name, phone, email, address])
    save_contacts(contacts)

    contact_listbox.insert(tk.END, name)
    clear_entries()
    messagebox.showinfo("Success", "Contact added successfully!")

# Function to display selected contact details
def display_contact(event):
    selected_index = contact_listbox.curselection()
    if not selected_index:
        return
    index = selected_index[0]

    contacts = load_contacts()
    name, phone, email, address = contacts[index]

    name_entry.delete(0, tk.END)
    name_entry.insert(0, name)

    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, phone)

    email_entry.delete(0, tk.END)
    email_entry.insert(0, email)

    address_entry.delete(0, tk.END)
    address_entry.insert(0, address)

# Function to update a contact
def update_contact():
    selected_index = contact_listbox.curselection()
    if not selected_index:
        messagebox.showerror("Error", "No contact selected!")
        return
    index = selected_index[0]

    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if not name or not phone:
        messagebox.showerror("Error", "Name and Phone Number are required!")
        return

    contacts = load_contacts()
    contacts[index] = [name, phone, email, address]
    save_contacts(contacts)

    contact_listbox.delete(index)
    contact_listbox.insert(index, name)
    messagebox.showinfo("Success", "Contact updated successfully!")

# Function to delete a contact
def delete_contact():
    selected_index = contact_listbox.curselection()
    if not selected_index:
        messagebox.showerror("Error", "No contact selected!")
        return
    index = selected_index[0]

    contacts = load_contacts()
    del contacts[index]
    save_contacts(contacts)

    contact_listbox.delete(index)
    clear_entries()
    messagebox.showinfo("Success", "Contact deleted successfully!")

# Function to search contacts
def search_contact():
    query = search_entry.get().strip().lower()
    contact_listbox.delete(0, tk.END)
    
    contacts = load_contacts()
    for contact in contacts:
        if query in contact[0].lower() or query in contact[1]:  # Search by name or phone
            contact_listbox.insert(tk.END, contact[0])

# Function to clear input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Main application window
root = tk.Tk()
root.title("Contact Book")
root.geometry("1000x500")
root.config(bg="lightblue")

# Contact Form
frame = tk.Frame(root, bg="white", padx=10, pady=10, width=150, background="lightblue")
frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

nameTxt = tk.Label(frame, text="Name:", font=("Arial", 12), bg="white")
nameTxt.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame, width=30, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=5, pady=5)

phoneTxt = tk.Label(frame, text="Phone:", font=("Arial", 12), bg="white")
phoneTxt.grid(row=1, column=0, padx=5, pady=5)
phone_entry = tk.Entry(frame, width=30, font=("Arial", 12))
phone_entry.grid(row=1, column=1, padx=5, pady=5)

emailTxt = tk.Label(frame, text="Email:", font=("Arial", 12), bg="white")
emailTxt.grid(row=2, column=0, padx=5, pady=5)
email_entry = tk.Entry(frame, width=30, font=("Arial", 12))
email_entry.grid(row=2, column=1, padx=5, pady=5)

addressTxt = tk.Label(frame, text="Address:", font=("Arial", 12), bg="white")
addressTxt.grid(row=3, column=0, padx=5, pady=5)
address_entry = tk.Entry(frame, width=30, font=("Arial", 12))
address_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Button(frame, text="Add", font=("Arial", 12), bg="green", fg="white", command=add_contact).grid(row=4, column=0, padx=5, pady=5, ipady=10, ipadx=20)
tk.Button(frame, text="Update", font=("Arial", 12), bg="blue", fg="white", command=update_contact).grid(row=4, column=1, padx=5, pady=5, ipady=10, ipadx=20)
tk.Button(frame, text="Delete", font=("Arial", 12), bg="red", fg="white", command=delete_contact).grid(row=4, column=2, padx=5, pady=5, ipady=10, ipadx=20)


# Contact Listbox
list_frame = tk.Frame(root, bg="white", pady=10, background="blue", width=850)
list_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Search
search_entry = tk.Entry(list_frame, width=40, font=("Arial", 12))
search_entry.grid(row=0, column=0, columnspan=1, padx=5, ipady=12)

searchBtn =tk.Button(list_frame, text="Search", bg="#FFA07A", font=("Arial", 12))
searchBtn.grid(row=0, column=1, columnspan=1, padx=15, pady=10, ipadx=10, ipady=12)

contact_listbox = tk.Listbox(list_frame, width=50, font=("Arial", 12), bg="lightblue", height=20)
contact_listbox.grid(row=1, column=0, columnspan=2)
contact_listbox.bind("<<ListboxSelect>>", display_contact)

nameTxt = tk.Label(list_frame, text="Developed By : Prof. Hezzy", fg="#fff", bg="blue", font=("Arial", 13))
nameTxt.grid(row=2, column=0, columnspan=2)

# Load contacts into Listbox
for contact in load_contacts():
    contact_listbox.insert(tk.END, contact[0])

root.mainloop()
