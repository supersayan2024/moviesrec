from models.employee import Employee

class AuthController:
    def __init__(self):
        self.employees = [
            Employee(name="Doe", first_name="John", gender="Male", hire_date="2021-01-01", user_code="jdoe", password="password123", access_type="full"),
            Employee(name="Smith", first_name="Jane", gender="Female", hire_date="2020-05-15", user_code="jsmith", password="password456", access_type="read"),
        ]

    def authenticate(self, user_code, password):
        for employee in self.employees:
            if employee.user_code == user_code and employee.password == password:
                return True
        return False

    def get_access_type(self, user_code):
        for employee in self.employees:
            if employee.user_code == user_code:
                return employee.access_type
        return None
