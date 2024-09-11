from django.db import models
from user_management.models import CustomUser
from parking_spot.models import ParkingSpot
from datetime import datetime

class Ticket(models.Model):
    ticket_number = models.CharField(max_length=20, unique=True, blank=True)
    entry_time = models.DateTimeField()
    exit_time = models.DateTimeField(null=True, blank=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    license_plate = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        # Générer le ticket_number si non présent
        if not self.ticket_number:
            now = datetime.now()
            date_part = now.strftime('%y%m%d%f')[:9]  # Format YYMMDDms
            self.ticket_number = f"P01-{date_part}"
        
        super().save(*args, **kwargs)
            
    def __str__(self):
        return f"Ticket n°{self.ticket_number}"