from django.db import models
from django.utils import timezone
from ticket.models import Ticket

class History(models.Model):
    event_type = models.CharField(max_length=50)  # Exemple: "Modification", "Paiement", "Annulation"
    description = models.TextField()
    recorded_at = models.DateTimeField(default=timezone.now)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.event_type} - {self.ticket}'
