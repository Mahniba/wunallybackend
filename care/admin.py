from django.contrib import admin

from .models import CarePlanNotes, EmergencyContact, Reminder


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "time", "completed", "client_id")
    list_filter = ("completed", "icon_type")


@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "phone", "client_id")
    search_fields = ("name", "phone", "user__email")


@admin.register(CarePlanNotes)
class CarePlanNotesAdmin(admin.ModelAdmin):
    list_display = ("user", "updated_at")
