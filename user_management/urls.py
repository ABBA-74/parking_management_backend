from rest_framework import routers
from user_management.views import UserDetailView

router = routers.DefaultRouter()
router.register('profile', UserDetailView, basename='user-profile')