from django.test import TestCase
from .models import ParkingSpot
from django.contrib.auth.models import User

class ParkingSpotModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="testuser", first_name="John", last_name="Doe")
        self.parking_spot = ParkingSpot.objects.create(spot_number="A1", user=self.user)

    def test_parking_spot_creation(self):
        """Test si une place de parking peut être créée"""
        self.assertEqual(self.parking_spot.spot_number, "A1")
        self.assertEqual(self.parking_spot.user.username, "testuser")

    def test_parking_spot_str_representation(self):
        """Test si la représentation string de la place de parking est correcte"""
        self.assertEqual(str(self.parking_spot), "La place de parking n°A1 est disponible")
