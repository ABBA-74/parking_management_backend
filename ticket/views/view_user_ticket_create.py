from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import generics
from ..models import Ticket
from ..serializers import TicketSerializer
from drf_yasg.utils import swagger_auto_schema 

from rest_framework.response import Response
from rest_framework import status
from parking_spot.models import ParkingSpot
from drf_yasg import openapi


# Vue pour générer un nouveau ticket par l'utilisateur de l'application
class UserTicketCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(
        operation_description="Create a new parking ticket by providing the parking spot number",
        tags=["Ticket"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'spot_number': openapi.Schema(type=openapi.TYPE_STRING, description='Parking spot number'),
                'entry_time': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Entry time'),
                'license_plate': openapi.Schema(type=openapi.TYPE_STRING, description='License plate of the vehicle'),
            },
            required=['spot_number', 'entry_time', 'license_plate']
        ),
        responses={
            201: TicketSerializer,
            400: 'Bad Request',
            404: 'Place de parking non trouvé',
            409: 'Place de parking déjà occupée'
        }
    )
    def post(self, request, *args, **kwargs):
        # Récupérer le numéro de la place depuis la requête
        spot_number = request.data.get('spot_number')
        
        try:
            # Rechercher la place de parking correspondante
            parking_spot = ParkingSpot.objects.get(spot_number=spot_number)
        except ParkingSpot.DoesNotExist:
            return Response({'error': 'Place de parking non trouvé'}, status=status.HTTP_404_NOT_FOUND)

        if parking_spot.is_occupied:
            return Response({'error': 'Place de parking déjà occupée'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Créer un nouveau ticket
        ticket_data = request.data
        ticket_data['parking_spot'] = parking_spot.id  # Associer la place de parking
        ticket_data['user'] = request.user.id if request.user.is_authenticated else None
        
        serializer = self.get_serializer(data=ticket_data)
        if serializer.is_valid():
            serializer.save()
            # Marquer la place comme occupée
            parking_spot.is_occupied = True
            parking_spot.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
