import tkinter as tk
from tkinter import ttk
from views.customer_creation_window import CustomerCreationWindow
from views.customer_modification_window import CustomerModificationWindow

class MainWindow:
    def __init__(self, root, customer_controller, movie_controller):
        self.root = root
        self.root.title("Main Window")
        self.customer_controller = customer_controller
        self.movie_controller = movie_controller

        # Customer List
        self.label_customers = tk.Label(root, text="Customers")
        self.label_customers.pack(pady=10)

        self.customer_table = ttk.Treeview(root, columns=("First Name", "Last Name", "Email"), show='headings')
        self.customer_table.heading("First Name", text="First Name")
        self.customer_table.heading("Last Name", text="Last Name")
        self.customer_table.heading("Email", text="Email")
        self.customer_table.pack(pady=10)

        self.populate_customers()

        # Movie List
        self.label_movies = tk.Label(root, text="Movies")
        self.label_movies.pack(pady=10)

        self.movie_table = ttk.Treeview(root, columns=("Name", "Duration", "Categories"), show='headings')
        self.movie_table.heading("Name", text="Name")
        self.movie_table.heading("Duration", text="Duration")
        self.movie_table.heading("Categories", text="Categories")
        self.movie_table.pack(pady=10)

        self.populate_movies()

        # Buttons
        self.button_create_customer = tk.Button(root, text="Create Customer", command=self.create_customer)
        self.button_create_customer.pack(pady=5)

        self.button_edit_customer = tk.Button(root, text="Edit Customer", command=self.edit_customer)
        self.button_edit_customer.pack(pady=5)

        self.button_delete_customer = tk.Button(root, text="Delete Customer", command=self.delete_customer)
        self.button_delete_customer.pack(pady=5)

    def populate_customers(self):
        for customer in self.customer_controller.get_all_customers():
            self.customer_table.insert("", "end", values=(customer.first_name, customer.name, customer.email))

    def populate_movies(self):
        for movie in self.movie_controller.get_all_movies():
            categories = ", ".join([category.name for category in movie.categories])
            self.movie_table.insert("", "end", values=(movie.name, movie.duration, categories))

    def create_customer(self):
        customer_creation_window = tk.Toplevel(self.root)
        CustomerCreationWindow(customer_creation_window, self.customer_controller)
        customer_creation_window.wait_window()
        self.refresh_customers()

    def edit_customer(self):
        selected_item = self.customer_table.selection()
        if not selected_item:
            return
        customer_email = self.customer_table.item(selected_item[0], "values")[2]
        customer = self.customer_controller.find_customer_by_email(customer_email)

        customer_modification_window = tk.Toplevel(self.root)
        CustomerModificationWindow(customer_modification_window, customer, self.customer_controller)
        customer_modification_window.wait_window()
        self.refresh_customers()

    def delete_customer(self):
        selected_item = self.customer_table.selection()
        if not selected_item:
            return
        customer_email = self.customer_table.item(selected_item[0], "values")[2]
        customer = self.customer_controller.find_customer_by_email(customer_email)

        self.customer_controller.delete_customer(customer)
        self.refresh_customers()

    def refresh_customers(self):
        for i in self.customer_table.get_children():
            self.customer_table.delete(i)
        self.populate_customers()