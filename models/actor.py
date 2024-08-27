from models.person import Person

class Actor(Person):
    def __init__(self, name: str, first_name: str, gender: str, character_name: str, start_of_employment: str, end_of_employment: str, stamp: float):
        super().__init__(name, first_name, gender)
        self.character_name = character_name
        self.start_of_employment = start_of_employment
        self.end_of_employment = end_of_employment
        self.stamp = stamp

    def __str__(self):
        return f"{super().__str__()} | Character: {self.character_name}"

    def display_info(self):
        super().display_info()
        print(f"Character Name: {self.character_name}")
        print(f"Start of Employment: {self.start_of_employment}")
        print(f"End of Employment: {self.end_of_employment}")
        print(f"Stamp: ${self.stamp:.2f}")
ex3 = Actor("imam", "dan", "mas", "im", "26aout2024", "26aout2025", 5.1)
ex3.display_info()
print(ex3)