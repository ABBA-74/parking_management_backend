from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import generics
from .models import History
from .serializers import HistorySerializer
from drf_yasg.utils import swagger_auto_schema 

class HistoryListCreateView(generics.ListCreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(operation_description="List of all histories", tags=["History"])
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new history", tags=["History"])
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)

class HistoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = History.objects.all()
    serializer_class =HistorySerializer
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(operation_description="Consult a history", tags=["History"])
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @swagger_auto_schema(operation_description="Update a history", tags=["History"])
    def put(self, *args, **kwargs):
        return super().put(*args, **kwargs)
    
    @swagger_auto_schema(operation_description="Partial update of a history", tags=["History"])
    def patch(self, *args, **kwargs):
        return super().patch(*args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a history", tags=["History"])
    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)
