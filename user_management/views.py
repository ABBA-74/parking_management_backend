from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from user_management.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema 

class UserDetailView(viewsets.ViewSet):
    
    @swagger_auto_schema(operation_description="List of information on logged-in users", tags=["Profile"])
    def list(self, request):
        user = request.user
        user_data = UserSerializer(user, context={'request': request}).data
        return Response(user_data)
