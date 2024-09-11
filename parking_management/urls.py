"""
URL configuration for parking_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import routers
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from parking_management import settings

from user_management.urls import router as user_management_router
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include

schema_view = get_schema_view(
   openapi.Info(
      title="API Parking Management",
      default_version='v1',
      description="Documentation for parking management API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@parking.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=[], 
)

router = routers.DefaultRouter()
router.registry.extend(user_management_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
    path('auth/', include('dj_rest_auth.urls')),
    path('api/', include('pricing.urls')),
    path('api/', include('parking_spot.urls')),
    path('api/', include('ticket.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
