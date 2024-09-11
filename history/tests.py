from django.test import TestCase
from .models import History
from ticket.models import Ticket
from datetime import datetime

class HistoryModelTest(TestCase):

    def setUp(self):
        self.ticket = Ticket.objects.create(ticket_number="P01-2409112395", entry_time=datetime.now(),)
        self.history = History.objects.create(
            event_type="Modification",
            description="Le ticket a été modifié",
            ticket=self.ticket
        )

    def test_history_creation(self):
        """Test si un événement dans l'historique peut être créé"""
        self.assertEqual(self.history.event_type, "Modification")
        self.assertEqual(self.history.description, "Le ticket a été modifié")
    
    def test_history_str_representation(self):
        """Test si la représentation string de l'historique est correcte"""
        self.assertEqual(str(self.history), "Modification - Ticket n°P01-2409112395")
