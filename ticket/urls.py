from django.urls import path
from .views import TicketDetailView, TicketExitView, TicketListCreateView, TicketPriceView, UserTicketCreateView 

urlpatterns = [
    path('ticket/', TicketListCreateView.as_view(), name='ticket-list-create'),
    path('ticket-create/', UserTicketCreateView.as_view(), name='ticket-create'),
    path('ticket-exit/', TicketExitView.as_view(), name='ticket-create'),
    path('ticket-price/', TicketPriceView.as_view(), name='ticket-create'),
    path('ticket/<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
]