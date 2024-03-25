from django.test import TestCase

from auth import services
from auth.errors import InvalidCredentials
from users.tests.factories import UserFactory


class TestServices(TestCase):
    """
    Test case for auth services.
    """
    def test_login(self):
        new_user = UserFactory()
        user = services.login(username=new_user.username,
                              password='testpass123')
        self.assertIsNotNone(user)
        self.assertEqual(user, new_user)
    
    def test_login_fail_user_does_not_exist(self):
        with self.assertRaises(InvalidCredentials):
            services.login(username='bob',
                           password='testpass123')
    
    def test_login_fail_wrong_password(self):
        user = UserFactory()
        with self.assertRaises(InvalidCredentials):
            services.login(username=user.username,
                           password='wrongpassword')
