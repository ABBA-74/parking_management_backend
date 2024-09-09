from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import generics
from .models import ParkingSpot
from .serializers import ParkingSpotSerializer
from drf_yasg.utils import swagger_auto_schema 

class ParkingSpotListCreateView(generics.ListCreateAPIView):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer

    @swagger_auto_schema(operation_description="List of all parking spots", tags=["Parking Spot"])
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new parking spot", tags=["Parking Spot"])
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)

    def get_permissions(self):
        if self.request.method == 'POST': # Seuls les admins peuvent créer
            return [IsAdminUser()]
        return [AllowAny()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) # Admin qui crée la place de parking


class ParkingSpotManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer

    @swagger_auto_schema(operation_description="Consult a parking spot", tags=["Parking Spot"])
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @swagger_auto_schema(operation_description="Update a parking spot", tags=["Parking Spot"])
    def put(self, *args, **kwargs):
        return super().put(*args, **kwargs)
    
    @swagger_auto_schema(operation_description="Partial update of a parking spot", tags=["Parking Spot"])
    def patch(self, *args, **kwargs):
        return super().patch(*args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a parking spot", tags=["Parking Spot"])
    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)
    
    @swagger_auto_schema(tags=["Parking Spot"])
    def get_permissions(self):
        if self.request.method == 'DELETE': # Seuls les admins peuvent supprimer
            return [IsAdminUser()]
        return [AllowAny()]