from models.customer import Customer

class CustomerController:
    def __init__(self):
        self.customers = []

    def create_customer(self, first_name, last_name, email, password):
        if self.find_customer_by_email(email):
            raise ValueError("A customer with this email already exists.")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")

        customer = Customer(name=last_name, first_name=first_name, gender=None, registration_date=None, email=email, password=password)
        self.customers.append(customer)

    def update_customer(self, customer, first_name, last_name, email, password):
        if customer.email != email and self.find_customer_by_email(email):
            raise ValueError("A customer with this email already exists.")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")

        customer.first_name = first_name
        customer.name = last_name
        customer.email = email
        customer.password = password

    def delete_customer(self, customer):
        self.customers.remove(customer)

    def get_all_customers(self):
        return self.customers

    def find_customer_by_email(self, email):
        for customer in self.customers:
            if customer.email == email:
                return customer
        return None
