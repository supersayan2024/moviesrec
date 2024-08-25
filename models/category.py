class Category:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")