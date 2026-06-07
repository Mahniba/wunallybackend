from django.contrib import admin

from .models import AlertEvent, ChatMessage, SOSEvent


@admin.register(AlertEvent)
class AlertEventAdmin(admin.ModelAdmin):
    list_display = ("user", "symptom", "count", "window_days", "recorded_at")
    list_filter = ("symptom", "window_days")


@admin.register(SOSEvent)
class SOSEventAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "shared_location",
        "sms_sent",
        "contacts_notified_count",
        "recorded_at",
    )


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "mode", "input_mode", "created_at")
    list_filter = ("mode", "role")
