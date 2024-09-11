from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import time

class Pricing(models.Model):
    name = models.CharField(max_length=50)
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Admin qui a créé ou modifié, peut être nul
    
    def clean(self):
        # Vérifier que les horaires ne se chevauchent pas avec une autre tranche horaire
        if self.start_time == self.end_time:
            raise ValidationError("L'heure de début ne peut pas être égale à l'heure de fin.")

        # Récupérer les autres tranches existantes
        day_pricing = Pricing.objects.filter(name="Jour").exclude(id=self.id).first()
        night_pricing = Pricing.objects.filter(name="Nuit").exclude(id=self.id).first()

        if self.name == "Nuit":
            # Gestion spécifique de la nuit (tranche horaire qui traverse minuit)
            if not (self.end_time <= day_pricing.start_time or self.start_time >= day_pricing.end_time):
                raise ValidationError("Les horaires de nuit ne doivent pas chevaucher ceux de jour.")
            
            if self.start_time < time(12, 0):  # Exemple de validation supplémentaire : nuit commence après midi
                raise ValidationError("L'heure de début de la nuit doit être après midi.")

        if self.name == "Jour":
            # Gestion spécifique du jour (ne traverse pas minuit)
            if not (self.end_time <= night_pricing.start_time or self.start_time >= night_pricing.end_time):
                raise ValidationError("Les horaires de jour ne doivent pas chevaucher ceux de nuit.")
            
            if self.start_time != time(8, 0) or self.end_time != time(20, 0):  # Validation stricte des horaires de jour
                raise ValidationError("L'horaire de jour doit être entre 08h00 et 20h00.")

        
    def save(self, *args, **kwargs):
        # Exécuter les validations avant de sauvegarder
        self.clean()
        super().save(*args, **kwargs)
        
    def delete(self, *args, **kwargs):
        # Empêche la suppression des entrées Jour et Nuit
        if self.name in ['Jour', 'Nuit']:
            raise ValidationError(f"L'entrée '{self.name}' ne peut pas être supprimée.")
        else:
            super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.name}: {self.start_time} - {self.end_time}"