from tkinter import *
from tkinter import messagebox

# dictionary for contacts
contacts = {}

def add_contact():
    n = name_var.get()
    p = phone_var.get()
    e = email_var.get()
    a = address_var.get()

    if n == "" or p == "":
        messagebox.showwarning("Error", "Name and Phone required!")
        return

    contacts[n] = {"phone": p, "email": e, "address": a}
    update_list()
    name_var.set(""); phone_var.set(""); email_var.set(""); address_var.set("")

def update_list():
    listbox.delete(0, END)
    for n, d in contacts.items():
        listbox.insert(END, n + " - " + d["phone"])

def search():
    s = search_var.get().lower()
    listbox.delete(0, END)
    for n, d in contacts.items():
        if s in n.lower() or s in d["phone"]:
            listbox.insert(END, n + " - " + d["phone"])

def show_details(e):
    sel = listbox.curselection()
    if sel:
        n = listbox.get(sel[0]).split(" - ")[0]
        d = contacts[n]
        messagebox.showinfo("Details", f"Name: {n}\nPhone: {d['phone']}\nEmail: {d['email']}\nAddress: {d['address']}")

def delete_contact():
    sel = listbox.curselection()
    if sel:
        n = listbox.get(sel[0]).split(" - ")[0]
        if messagebox.askyesno("Delete", "Delete " + n + "?"):
            del contacts[n]
            update_list()

# main window
root = Tk()
root.title("Contact Book")
root.geometry("400x500")

name_var = StringVar()
phone_var = StringVar()
email_var = StringVar()
address_var = StringVar()
search_var = StringVar()

Label(root, text="Name").pack()
Entry(root, textvariable=name_var).pack()
Label(root, text="Phone").pack()
Entry(root, textvariable=phone_var).pack()
Label(root, text="Email").pack()
Entry(root, textvariable=email_var).pack()
Label(root, text="Address").pack()
Entry(root, textvariable=address_var).pack()

Button(root, text="Add", command=add_contact, bg="green", fg="white").pack(pady=5)

Label(root, text="Search").pack()
Entry(root, textvariable=search_var).pack()
Button(root, text="Search", command=search, bg="blue", fg="white").pack(pady=5)

listbox = Listbox(root, width=40, height=10)
listbox.pack(pady=10)
listbox.bind("<Double-1>", show_details)

Button(root, text="Delete", command=delete_contact, bg="red", fg="white").pack(pady=5)

root.mainloop()
