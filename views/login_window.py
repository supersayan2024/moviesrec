import tkinter

import  tkinter as tk
from tkinter import messagebox
from views.main_window import MainWindow
from controllers.customer_controller import CustomerController
from controllers.movie_controller import MovieController

class LoginWindow:
    def __init__(self, root, auth_controller):
        self.root = root
        self.root.title("Login")
        self.auth_controller = auth_controller

        self.label_user_code = tk.Label(root, text="User Code")
        self.label_user_code.pack(pady=10)

        self.entry_user_code = tk.Entry(root)
        self.entry_user_code.pack(pady=5)

        self.label_password = tk.Label(root, text="Password")
        self.label_password.pack(pady=10)

        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack(pady=5)

        self.button_login = tk.Button(root, text="Login", command=self.login)
        self.button_login.pack(pady=20)

    def login(self):
        user_code = self.entry_user_code.get()
        password = self.entry_password.get()

        if self.auth_controller.authenticate(user_code, password):
            access_type = self.auth_controller.get_access_type(user_code)
            messagebox.showinfo("Login Successful", "Welcome!")
            self.root.destroy()
            self.open_main_window(access_type)
        else:
            messagebox.showerror("Login Failed", "Invalid User Code or Password")

    def open_main_window(self, access_type):
        main_root = tk.Tk()  # Create a new Tkinter root for the main window
        customer_controller = CustomerController()
        movie_controller = MovieController()
        MainWindow(main_root, customer_controller, movie_controller)  # Pass controllers to MainWindow
        main_root.mainloop()  # Start the Tkinter event loop for the main window