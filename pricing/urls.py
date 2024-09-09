from django.urls import path
from .views import PricingListCreateView, PricingDetailView

urlpatterns = [
    path('pricing/', PricingListCreateView.as_view(), name='pricing-list-create'),
    path('pricing/<int:pk>/', PricingDetailView.as_view(), name='pricing-detail'),
]