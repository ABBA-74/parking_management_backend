from django.contrib import admin
from .models import History

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_type', 'get_ticket_number', 'description', 'recorded_at')
    list_filter = ('event_type', 'recorded_at')
    search_fields = ('event_type', 'ticket__ticket_number')
        
    def get_ticket_number(self, obj):
        return obj.ticket.ticket_number if obj.ticket else None
    get_ticket_number.short_description = 'Ticket Number'

admin.site.register(History, HistoryAdmin)