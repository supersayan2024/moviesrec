import unittest
from controllers.customer_controller import CustomerController
from models.customer import Customer

class TestCustomerController(unittest.TestCase):
    def setUp(self):
        self.customer_controller = CustomerController()

    def test_create_customer(self):
        self.customer_controller.create_customer("John", "Doe", "johndoe@example.com", "password123")
        customer = self.customer_controller.find_customer_by_email("johndoe@example.com")
        self.assertIsNotNone(customer)
        self.assertEqual(customer.email, "johndoe@example.com")

    def test_create_customer_with_existing_email(self):
        self.customer_controller.create_customer("Jane", "Smith", "janesmith@example.com", "password123")
        with self.assertRaises(ValueError):
            self.customer_controller.create_customer("John", "Doe", "janesmith@example.com", "password456")

    def test_create_customer_with_short_password(self):
        with self.assertRaises(ValueError):
            self.customer_controller.create_customer("John", "Doe", "johndoe@example.com", "short")

    def test_update_customer(self):
        self.customer_controller.create_customer("John", "Doe", "johndoe@example.com", "password123")
        customer = self.customer_controller.find_customer_by_email("johndoe@example.com")
        self.customer_controller.update_customer(customer, "Johnny", "Doe", "johnnydoe@example.com", "newpassword123")
        updated_customer = self.customer_controller.find_customer_by_email("johnnydoe@example.com")
        self.assertIsNotNone(updated_customer)
        self.assertEqual(updated_customer.first_name, "Johnny")

    def test_delete_customer(self):
        self.customer_controller.create_customer("John", "Doe", "johndoe@example.com", "password123")
        customer = self.customer_controller.find_customer_by_email("johndoe@example.com")
        self.customer_controller.delete_customer(customer)
        deleted_customer = self.customer_controller.find_customer_by_email("johndoe@example.com")
        self.assertIsNone(deleted_customer)

if __name__ == "__main__":
    unittest.main()