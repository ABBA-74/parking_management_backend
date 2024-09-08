from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from user_management.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class UserDetailView(viewsets.ViewSet):
    
    # permission_classes = (IsAuthenticated, )
    def list(self, request):
        user = User.objects.get(username=request.user)
        user_data = UserSerializer(user, context={'request': request}).data
        return Response(user_data)
