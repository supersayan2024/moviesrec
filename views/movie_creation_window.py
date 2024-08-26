# views/movie_creation_window.py
import tkinter as tk
from tkinter import messagebox

class MovieCreationWindow:
    def __init__(self, root, movie_controller):
        self.root = root
        self.movie_controller = movie_controller
        self.root.title("Create Movie")

        self.label_name = tk.Label(root, text="Movie Name:")
        self.label_name.pack(pady=5)
        self.entry_name = tk.Entry(root)
        self.entry_name.pack(pady=5)

        self.label_duration = tk.Label(root, text="Duration (minutes):")
        self.label_duration.pack(pady=5)
        self.entry_duration = tk.Entry(root)
        self.entry_duration.pack(pady=5)

        self.label_description = tk.Label(root, text="Description:")
        self.label_description.pack(pady=5)
        self.entry_description = tk.Entry(root)
        self.entry_description.pack(pady=5)

        self.label_categories = tk.Label(root, text="Categories (comma-separated):")
        self.label_categories.pack(pady=5)
        self.entry_categories = tk.Entry(root)
        self.entry_categories.pack(pady=5)

        self.button_create = tk.Button(root, text="Create", command=self.create_movie)
        self.button_create.pack(pady=20)

    def create_movie(self):
        name = self.entry_name.get()
        duration = int(self.entry_duration.get())
        description = self.entry_description.get()
        categories = self.entry_categories.get().split(',')

        try:
            self.movie_controller.create_movie(name, duration, description, categories)
            messagebox.showinfo("Success")
            messagebox.showinfo("Success", "Movie created successfully!")
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create movie: {str(e)}")
