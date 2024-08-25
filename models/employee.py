from models.person import Person

class Employee(Person):
    def __init__(self, name: str, first_name: str, gender: str, hire_date: str, user_code: str, password: str, access_type: str):
        super().__init__(name, first_name, gender)
        self.hire_date = hire_date  # Changed from hiring_date to hire_date
        self.user_code = user_code
        self.password = password
        self.access_type = access_type

    def __str__(self):
        return f"{super().__str__()} | User Code: {self.user_code}"

    def display_info(self):
        super().display_info()
        print(f"Hire Date: {self.hire_date}")  # Updated to match the attribute name
        print(f"User Code: {self.user_code}")
        print(f"Access Type: {self.access_type}")