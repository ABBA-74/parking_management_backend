from django.test import TestCase
from .models import Pricing
class PricingModelTest(TestCase):

    def setUp(self):
        self.pricing = Pricing.objects.create(
            name="Test",
            hourly_rate=2.4,
            start_time="08:00",
            end_time="20:00"
        )

    def test_pricing_creation(self):
        """Test si un tarif peut être créé"""
        self.assertEqual(self.pricing.name, "Test")
        self.assertEqual(self.pricing.hourly_rate, 2.4)
    
    def test_pricing_str_representation(self):
        """Test si la représentation string du tarif est correcte"""
        self.assertEqual(str(self.pricing), "Test: 08:00 - 20:00")
