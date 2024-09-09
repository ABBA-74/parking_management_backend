from django.shortcuts import render

from rest_framework import generics
from .models import Pricing
from .serializers import PricingSerializer
from rest_framework.permissions import IsAdminUser

# Vue pour lister et créer des tarifications
class PricingListCreateView(generics.ListCreateAPIView):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer
    permission_classes = [IsAdminUser]

# Vue pour récupérer, mettre à jour, ou supprimer une tarification
class PricingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer
    permission_classes = [IsAdminUser]