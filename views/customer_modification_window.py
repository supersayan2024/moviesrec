import tkinter as tk
from tkinter import messagebox

class CustomerModificationWindow:
    def __init__(self, root, customer, customer_controller):
        self.root = root
        self.root.title("Edit Customer")
        self.customer = customer
        self.customer_controller = customer_controller

        self.label_first_name = tk.Label(root, text="First Name")
        self.label_first_name.pack(pady=10)

        self.entry_first_name = tk.Entry(root)
        self.entry_first_name.insert(0, customer.first_name)
        self.entry_first_name.pack(pady=5)

        self.label_last_name = tk.Label(root, text="Last Name")
        self.label_last_name.pack(pady=10)

        self.entry_last_name = tk.Entry(root)
        self.entry_last_name.insert(0, customer.name)
        self.entry_last_name.pack(pady=5)

        self.label_email = tk.Label(root, text="Email")
        self.label_email.pack(pady=10)

        self.entry_email = tk.Entry(root)
        self.entry_email.insert(0, customer.email)
        self.entry_email.pack(pady=5)

        self.label_password = tk.Label(root, text="Password")
        self.label_password.pack(pady=10)

        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.insert(0, customer.password)
        self.entry_password.pack(pady=5)

        self.button_update = tk.Button(root, text="Update", command=self.update_customer)
        self.button_update.pack(pady=20)

    def update_customer(self):
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        try:
            self.customer_controller.update_customer(self.customer, first_name, last_name, email, password)
            messagebox.showinfo("Success", "Customer updated successfully")
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
