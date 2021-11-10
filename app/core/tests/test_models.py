from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Asserting the the user is created successful as expected"""
        email = "teste@email.com"
        password = "Testepass@123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Asserting that the email is normalized during the user creation"""
        email = "test@EMAIL.COM"
        user = get_user_model().objects.create_user(email, "test@123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """
        Asserting that a error is raised when there is no e-mail for the user
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "test@123")

    def test_new_superuser(self):
        """Testing a superuser creation"""
        email = "admin@email.com"
        user = get_user_model().objects.create_superuser(email, "test@123")

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)