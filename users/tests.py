from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.core.exceptions import ValidationError
User = get_user_model()
class UserModelTests(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            email='john@example.com',
            firstname='John',
            lastname='Doe',
            password='securepassword123'
        )
        self.assertEqual(user.email, 'john@example.com')
        self.assertEqual(user.firstname, 'John')
        self.assertEqual(user.lastname, 'Doe')
        self.assertTrue(user.check_password('securepassword123'))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
            email='admin@example.com',
            firstname='Admin',
            lastname='User',
            password='supersecurepassword456'
        )
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
    def test_create_user_without_email(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email='',
                firstname='John',
                lastname='Doe',
                password='securepassword123'
            )
    def test_create_user_with_duplicate_email(self):
        User.objects.create_user(
            email='john@example.com',
            firstname='John',
            lastname='Doe',
            password='securepassword123'
        )
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                email='john@example.com',
                firstname='Another',
                lastname='User',
                password='anotherpassword'
            )
    def test_set_custom_role(self):
        user = User.objects.create_user(
            email='jane@example.com',
            firstname='Jane',
            lastname='Smith',
            password='userpassword789'
        )
        user.role = 'Agricultural_officer'
        user.save()
        self.assertEqual(user.role, 'Agricultural_officer')
    def test_set_invalid_role(self):
        user = User.objects.create_user(
            email='jane@example.com',
            firstname='Jane',
            lastname='Smith',
            password='userpassword789'
        )
        with self.assertRaises(ValidationError):
            user.role = 'InvalidRole'
            user.full_clean()
    def test_authenticate_user(self):
        User.objects.create_user(
            email='jane@example.com',
            firstname='Jane',
            lastname='Smith',
            password='userpassword789'
        )
        authenticated_user = self.client.login(email='jane@example.com', password='userpassword789')
        self.assertTrue(authenticated_user)
    def test_authenticate_with_wrong_password(self):
        User.objects.create_user(
            email='jane@example.com',
            firstname='Jane',
            lastname='Smith',
            password='userpassword789'
        )
        authenticated_user = self.client.login(email='jane@example.com', password='wrongpassword')
        self.assertFalse(authenticated_user)