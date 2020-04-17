from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelAddTest(TestCase):

    def test_create_user_by_email(self):
        """Test creating a new user with an email is successful"""
        email = "mohammad@gmail.com"
        password = "D123456_789"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_is_normalized(self):
        """Test a user email is normalized"""
        email = 'ali@Gmail.com'
        user = get_user_model().objects.create_user(email, '12523213M')

        self.assertEqual(user.email, email.lower())

    def test_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'ttetre')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'Ali@gmail.com',
            'test12346465'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)