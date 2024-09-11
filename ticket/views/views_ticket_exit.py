from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import generics
from ..models import Ticket
from ..serializers import TicketSerializer
from drf_yasg.utils import swagger_auto_schema 

from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi

# Vue pour libérer la place de parking et mettre à jour le ticket
class TicketExitView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Free up a parking spot by providing the ticket number",
        tags=["Ticket"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'ticket_number': openapi.Schema(type=openapi.TYPE_STRING, description='Ticket Number'),
            },
            required=['ticket_number']
        ),
        responses={
            201: TicketSerializer,
            400: 'Numéro de ticket requis',
            404: 'Numéro de ticket invalide',
            409: 'La place de parking a déjà été libéré'
        }
    )
    def post(self, request, *args, **kwargs):
        ticket_number = request.data.get('ticket_number')

        if not ticket_number:
            return Response({'error': 'Ticket number is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Récupérer le ticket correspondant au numéro fourni
        try:
            ticket = Ticket.objects.get(ticket_number=ticket_number)
        except Ticket.DoesNotExist:
            return Response({'error': 'Numéro de ticket invalide'}, status=status.HTTP_404_NOT_FOUND)

        # Vérifier si l'utilisateur a déjà quitté le parking
        if ticket.exit_time:
            return Response({'error': 'La place de parking a déjà été libéré'}, status=status.HTTP_409_CONFLICT)

        # Marquer la sortie et libérer la place
        ticket.exit_time = datetime.now()
        ticket.save(update_fields=['exit_time'])

        # Libérer la place de parking associée
        parking_spot = ticket.parking_spot
        if parking_spot:
            parking_spot.is_occupied = False
            parking_spot.save()

        return Response({'message': 'La place de parking a été libéré'}, status=status.HTTP_200_OK)