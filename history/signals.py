from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
from .models import History, Ticket

@receiver(post_delete, sender=Ticket)
def create_history_on_ticket_delete(sender, instance, **kwargs):
    History.objects.create(
        event_type="Suppression",
        description=f"Le ticket {instance.id} a été supprimé",
        ticket=None,
        recorded_at=timezone.now()
    )

@receiver(post_save, sender=Ticket)
def create_history_on_ticket_save(sender, instance, created, **kwargs):
    if created :
        History.objects.create(
            event_type="Création",
            description=f"Le ticket {instance.id} a été créé",
            ticket=instance,
            recorded_at=timezone.now()
        )
    else:
        History.objects.create(
            event_type="Modification",
            description=f"Le ticket {instance.id} a été modifié",
            ticket=instance,
            recorded_at=timezone.now()
        )