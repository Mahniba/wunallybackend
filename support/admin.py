from django.contrib import admin

from .models import AlertEvent, SOSEvent


@admin.register(AlertEvent)
class AlertEventAdmin(admin.ModelAdmin):
    list_display = ("user", "symptom", "count", "window_days", "recorded_at")
    list_filter = ("symptom", "window_days")


@admin.register(SOSEvent)
class SOSEventAdmin(admin.ModelAdmin):
    list_display = ("user", "shared_location", "recorded_at")
