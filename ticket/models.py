from django.db import models
from user_management.models import CustomUser
from parking_spot.models import ParkingSpot

class Ticket(models.Model):
    ticket_number = models.CharField(max_length=100, unique=True)
    entry_time = models.DateTimeField()
    exit_time = models.DateTimeField(null=True, blank=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    license_plate = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Ticket {self.ticket_number}"