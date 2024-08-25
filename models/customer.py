from models.person import Person

class Customer(Person):
    def __init__(self, name: str, first_name: str, gender: str, registration_date: str, email: str, password: str):
        super().__init__(name, first_name, gender)
        self.registration_date = registration_date
        self.email = email
        self.password = password
        self.credit_cards = []

    def add_credit_card(self, card):
        self.credit_cards.append(card)

    def __str__(self):
        return f"{super().__str__()} | Email: {self.email}"

    def display_info(self):
        super().display_info()
        print(f"Registration Date: {self.registration_date}")
        print(f"Email: {self.email}")
        print(f"Credit Cards: {', '.join([str(card) for card in self.credit_cards])}")