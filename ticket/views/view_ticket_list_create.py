from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import generics
from ..models import Ticket
from ..serializers import TicketSerializer
from rest_framework.permissions import IsAdminUser
from drf_yasg.utils import swagger_auto_schema 



# Vue pour lister et créer des tickets
class TicketListCreateView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    
    @swagger_auto_schema(operation_description="List of all tickets", tags=["Ticket"])
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new ticket", tags=["Ticket"])
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)
    
    def get_permissions(self):
        if self.request.method == 'POST': # Seuls les admins peuvent créer
            return [IsAdminUser()]
        return [AllowAny()]
