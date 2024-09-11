from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_number', 'license_plate', 'user_id', 'get_parking_spot_id', 'entry_time', 'exit_time', 'payment_amount')
    list_filter = ('entry_time', 'exit_time', 'user')
    search_fields = ('ticket_number', 'license_plate')

    def get_parking_spot_id(self, obj):
        return obj.parking_spot.id if obj.parking_spot else None
    get_parking_spot_id.short_description = 'Parking Spot ID'
    
admin.site.register(Ticket, TicketAdmin)
