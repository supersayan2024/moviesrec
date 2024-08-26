import unittest
from controllers.auth_controller import AuthController

class TestAuthController(unittest.TestCase):
    def setUp(self):
        self.auth_controller = AuthController()

    def test_authenticate_valid_user(self):
        result = self.auth_controller.authenticate(user_code="jdoe", password="password123")
        self.assertTrue(result)

    def test_authenticate_invalid_user(self):
        result = self.auth_controller.authenticate(user_code="jdoe", password="wrongpassword")
        self.assertFalse(result)

    def test_get_access_type(self):
        access_type = self.auth_controller.get_access_type(user_code="jdoe")
        self.assertEqual(access_type, "full")

    def test_get_access_type_invalid_user(self):
        access_type = self.auth_controller.get_access_type(user_code="invalid_user")
        self.assertIsNone(access_type)

if __name__ == "__main__":
    unittest.main()