class CardCredit:
    def __init__(self, card_number: str, expiration_date: str, secret_code: str):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.secret_code = secret_code

    def __str__(self):
        return f"Card {self.card_number} (Expires: {self.expiration_date})"

    def display_info(self):
        print(f"Card Number: {self.card_number}")
        print(f"Expiration Date: {self.expiration_date}")
        print(f"Secret Code: {self.secret_code}")