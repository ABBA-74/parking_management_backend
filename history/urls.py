from django.urls import path
from .views import HistoryListCreateView, HistoryDetailView

urlpatterns = [
    path('history/', HistoryListCreateView.as_view(), name='history-list-create'),
    path('history/<int:pk>/', HistoryDetailView.as_view(), name='history-manage'),
]
