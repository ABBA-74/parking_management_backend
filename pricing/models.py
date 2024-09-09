from django.db import models
from django.contrib.auth.models import User

class Pricing(models.Model):
    name = models.CharField(max_length=50)
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Admin qui a créé ou modifié, peut être nul

    def __str__(self):
        return self.name