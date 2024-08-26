import tkinter as tk
from views.login_window import LoginWindow
from controllers.auth_controller import AuthController


def main():
    # Initialize the Tkinter root window
    root = tk.Tk()

    # Initialize the authentication controller
    auth_controller = AuthController()

    # Initialize the login window with the root and auth_controller
    login_window = LoginWindow(root, auth_controller)

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
