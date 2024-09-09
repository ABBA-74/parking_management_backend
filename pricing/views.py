from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import generics
from .models import Pricing
from .serializers import PricingSerializer
from rest_framework.permissions import IsAdminUser
from drf_yasg.utils import swagger_auto_schema 

# Vue pour lister et créer des tarifications
class PricingListCreateView(generics.ListCreateAPIView):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer
    
    @swagger_auto_schema(operation_description="List of all ticket pricing", tags=["Pricing"])
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new ticket pricing", tags=["Pricing"])
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)
    
    def get_permissions(self):
        if self.request.method == 'POST': # Seuls les admins peuvent créer
            return [IsAdminUser()]
        return [AllowAny()]

# Vue pour récupérer, mettre à jour, ou supprimer une tarification
@swagger_auto_schema(tags=["Pricing"])
class PricingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(operation_description="Consult a ticket pricing", tags=["Pricing"])
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @swagger_auto_schema(operation_description="Update a ticket pricing", tags=["Pricing"])
    def put(self, *args, **kwargs):
        return super().put(*args, **kwargs)
    
    @swagger_auto_schema(operation_description="Partial update of a ticket pricing", tags=["Pricing"])
    def patch(self, *args, **kwargs):
        return super().patch(*args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a ticket pricing", tags=["Pricing"])
    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)
    
    def get_permissions(self):
        if self.request.method == 'DELETE': # Seuls les admins peuvent supprimer
            return [IsAdminUser()]
        return [AllowAny()]