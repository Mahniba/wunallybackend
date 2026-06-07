from django.contrib import admin

from .models import HealthFacility, HealthProvider, NurseAssignment


@admin.register(HealthProvider)
class HealthProviderAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "facility", "is_online", "active")
    list_filter = ("is_online", "role", "active")


@admin.register(NurseAssignment)
class NurseAssignmentAdmin(admin.ModelAdmin):
    list_display = ("user", "provider", "assigned_at", "active")


@admin.register(HealthFacility)
class HealthFacilityAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "region", "active")
