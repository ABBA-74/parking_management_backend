from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import generics
from ..models import Ticket
from ..serializers import TicketSerializer
from rest_framework.permissions import IsAdminUser
from drf_yasg.utils import swagger_auto_schema

# Vue pour récupérer, mettre à jour ou supprimer un ticket
class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    @swagger_auto_schema(operation_description="Consult a ticket", tags=["Ticket"])
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @swagger_auto_schema(operation_description="Update a ticket", tags=["Ticket"])
    def put(self, *args, **kwargs):
        return super().put(*args, **kwargs)
    
    @swagger_auto_schema(operation_description="Partial update of a ticket", tags=["Ticket"])
    def patch(self, *args, **kwargs):
        return super().patch(*args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a ticket", tags=["Ticket"])
    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)
    
    def get_permissions(self):
        if self.request.method == 'DELETE': # Seuls les admins peuvent supprimer
            return [IsAdminUser()]
        return [AllowAny()]
