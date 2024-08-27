class Person:
    def __init__(self, name: str, first_name: str, gender: str):
        self.name = name
        self.first_name = first_name
        self.gender = gender

    def __str__(self):
        return f"{self.first_name} {self.name} ({self.gender})"
    def display_info(self):
        print(f"Name: {self.first_name} {self.name}")
        print(f"Gender: {self.gender}")

ex=Person("david", "becha", "femme")
fa=Person("sebas", "gagnon", "homme")
print(ex.name)
fa.display_info()