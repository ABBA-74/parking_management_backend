from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.utils import timezone
from ..models import Ticket
from pricing.models import Pricing
from datetime import datetime, timedelta
from decimal import Decimal

class TicketPriceView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Get the price of a parking ticket by providing the ticket number",
        tags=["Ticket"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'ticket_number': openapi.Schema(type=openapi.TYPE_STRING, description='Ticket Number'),
            },
            required=['ticket_number']
        ),
        responses={
            200: 'Prix calculé avec succès',
            400: 'Numéro de ticket requis',
            404: 'Numéro de ticket invalide',
            409: 'Le ticket a déjà été payé'
        }
    )
    def post(self, request, *args, **kwargs):
        ticket_number = request.data.get('ticket_number')

        if not ticket_number:
            return Response({'error': 'Numéro de ticket requis'}, status=status.HTTP_400_BAD_REQUEST)

        # Récupérer le ticket correspondant au numéro fourni
        try:
            ticket = Ticket.objects.get(ticket_number=ticket_number)
        except Ticket.DoesNotExist:
            return Response({'error': 'Numéro de ticket invalide'}, status=status.HTTP_404_NOT_FOUND)

        # Vérifier si le ticket a déjà été payé (si exit_time est renseigné)
        if ticket.exit_time:
            return Response({'error': 'Le ticket a déjà été payé et la place a été libérée.'}, status=status.HTTP_409_CONFLICT)
        
        # Calculer la durée de stationnement
        entry_time = ticket.entry_time
        current_time = timezone.now()
    
        if ticket.entry_time.tzinfo is None:
            ticket.entry_time = timezone.make_aware(ticket.entry_time)
            
        duration = current_time - ticket.entry_time
        duration_in_hours = duration.total_seconds() / 3600  # Convertir en heures

        # Calculer le prix basé sur la durée
        day_pricing = Pricing.objects.get(name="Jour")
        night_pricing = Pricing.objects.get(name="Nuit")

        # Calcul du prix en fonction des tranches horaires
        total_price = 0
        current_slot_time = entry_time
        
        while current_slot_time < current_time:
            # Si on est dans la tranche "Jour"
            if day_pricing.start_time <= current_slot_time.time() < day_pricing.end_time:
                end_slot_time = min(current_time, timezone.make_aware(datetime.combine(current_slot_time.date(), day_pricing.end_time)))
                if end_slot_time <= current_slot_time:
                    end_slot_time += timedelta(days=1)  # Si l'heure de fin est passée au jour suivant
                
                duration_in_slot = (end_slot_time - current_slot_time).total_seconds() / 3600
                total_price += Decimal(duration_in_slot) * day_pricing.hourly_rate
                current_slot_time = end_slot_time
            else:
                # Si on est dans la tranche "Nuit"
                night_end_time = timezone.make_aware(datetime.combine(current_slot_time.date(), night_pricing.end_time))
                if night_end_time <= current_slot_time:
                    night_end_time += timedelta(days=1)  # Si l'heure de fin de la nuit est passée au jour suivant

                end_slot_time = min(current_time, night_end_time)
                duration_in_slot = (end_slot_time - current_slot_time).total_seconds() / 3600
                total_price += Decimal(duration_in_slot) * night_pricing.hourly_rate
                current_slot_time = end_slot_time

        return Response({
            'ticket_number': ticket.ticket_number,
            'entry_time': ticket.entry_time,
            'current_time': current_time,
            'total_duration_hours': round(duration_in_hours, 2),
            'total_price': round(total_price, 2)
        }, status=status.HTTP_200_OK)
