from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user():
    """Create a sample user"""
    return get_user_model().objects.create_user(
        email="test@email.com", password="testpass"
    )


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

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(user=sample_user(), name="Vegan")

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(), name="Cinnamon"
        )

        self.assertEqual(str(ingredient), ingredient.name)
