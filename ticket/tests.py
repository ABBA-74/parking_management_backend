from django.test import TestCase
from django.contrib.auth.models import User 
from .models import Ticket
from parking_spot.models import ParkingSpot
from user_management.models import CustomUser
from datetime import datetime

class TicketModelTest(TestCase):

    def setUp(self):
        self.parking_spot = ParkingSpot.objects.create(spot_number="A1")
        self.user_account = User.objects.create(username="testuser", first_name="John", last_name="Doe")
        self.user = CustomUser.objects.create(account=self.user_account)

        self.ticket = Ticket.objects.create(
            ticket_number="P01-2409112395",
            entry_time=datetime.now(),
            license_plate="ABC123",
            parking_spot=self.parking_spot,
            user=self.user
        )

    def test_ticket_creation(self):
        """Test si un ticket peut être créé"""
        self.assertEqual(self.ticket.ticket_number, "P01-2409112395")
        self.assertEqual(self.ticket.license_plate, "ABC123")
        self.assertEqual(self.ticket.user.account.username, "testuser")
    
    def test_ticket_str_representation(self):
        """Test si la représentation string du ticket est correcte"""
        self.assertEqual(str(self.ticket), "Ticket n°P01-2409112395")
