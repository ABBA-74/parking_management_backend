from django.urls import path
from .views import ParkingSpotManageView, ParkingSpotListCreateView

urlpatterns = [
    path('parking-spot/', ParkingSpotListCreateView.as_view(), name='parking-spot-list-create'),
    path('parking-spot/<int:pk>/', ParkingSpotManageView.as_view(), name='parking-spot-manage'),
]