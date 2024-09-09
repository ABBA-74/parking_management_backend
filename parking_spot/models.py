from django.db import models
from django.contrib.auth.models import User

class ParkingSpot(models.Model):
    spot_number = models.CharField(max_length=10, unique=True)
    is_occupied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Admin qui a créé ou modifié, peut être nul

    def __str__(self):
        return f"La place de parking n°{self.spot_number} est {'occupé' if self.is_occupied else 'disponible'}"