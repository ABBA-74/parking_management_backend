from django.test import TestCase
from django.contrib.auth.models import User
from user_management.models import CustomUser

class CustomUserModelTest(TestCase):

    def setUp(self):
        self.user_account = User.objects.create(
            username="testuser",
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com"
        )

        self.custom_user = CustomUser.objects.create(
            account=self.user_account,
            phone="+33612345678",
            address="123 Rue de la Poste",
            postal_code="74000",
            city="Annecy"
        )

    def test_custom_user_creation(self):
        """Test si un CustomUser peut être créé"""
        self.assertEqual(self.custom_user.phone, "+33612345678")
        self.assertEqual(self.custom_user.address, "123 Rue de la Poste")
        self.assertEqual(self.custom_user.postal_code, "74000")
        self.assertEqual(self.custom_user.city, "Annecy")

    def test_custom_user_str_representation(self):
        """Test si la représentation string de CustomUser est correcte"""
        self.assertEqual(str(self.custom_user), "John Doe")

    def test_custom_user_associated_account(self):
        """Test si l'utilisateur CustomUser est bien associé à un compte User"""
        self.assertEqual(self.custom_user.account.username, "testuser")
        self.assertEqual(self.custom_user.account.email, "john.doe@example.com")
