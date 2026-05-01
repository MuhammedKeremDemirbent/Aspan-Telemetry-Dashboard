from django.contrib import admin
from .models import SensorData

@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'created_at')
    search_fields = ('device_id',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
