from django.contrib import admin
from .models import Pricing

class PricingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hourly_rate', 'start_time', 'end_time', 'user_id', 'created_at', 'updated_at')
    list_filter = ('start_time', 'end_time', 'user')
    search_fields = ('name', 'user__username')

    # Interdire la suppression des lignes avec 'Jour' et 'Nuit'
    def has_delete_permission(self, request, obj=None):
        if obj and obj.name in ['Jour', 'Nuit']:
            return False
        return super().has_delete_permission(request, obj)

admin.site.register(Pricing, PricingAdmin)
