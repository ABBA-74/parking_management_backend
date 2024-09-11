from django.contrib import admin
from .models import ParkingSpot

class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ('id', 'spot_number', 'is_occupied', 'user_id', 'created_at', 'updated_at')
    list_filter = ('is_occupied', 'user')
    search_fields = ('spot_number', 'user__username')

admin.site.register(ParkingSpot, ParkingSpotAdmin)
