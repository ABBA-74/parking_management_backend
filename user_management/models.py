from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(region='FR', blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    postal_code = models.CharField(max_length=8, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
