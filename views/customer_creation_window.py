import tkinter as tk
from tkinter import messagebox

class CustomerCreationWindow:
    def __init__(self, root, customer_controller):
        self.root = root
        self.root.title("Create Customer")
        self.customer_controller = customer_controller

        self.label_first_name = tk.Label(root, text="First Name")
        self.label_first_name.pack(pady=10)

        self.entry_first_name = tk.Entry(root)
        self.entry_first_name.pack(pady=5)

        self.label_last_name = tk.Label(root, text="Last Name")
        self.label_last_name.pack(pady=10)

        self.entry_last_name = tk.Entry(root)
        self.entry_last_name.pack(pady=5)

        self.label_email = tk.Label(root, text="Email")
        self.label_email.pack(pady=10)

        self.entry_email = tk.Entry(root)
        self.entry_email.pack(pady=5)

        self.label_password = tk.Label(root, text="Password")
        self.label_password.pack(pady=10)

        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack(pady=5)

        self.button_create = tk.Button(root, text="Create", command=self.create_customer)
        self.button_create.pack(pady=20)

    def create_customer(self):
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        try:
            self.customer_controller.create_customer(first_name, last_name, email, password)
            messagebox.showinfo("Success", "Customer created successfully")
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))