from django.contrib import admin

from .models import MoodEntry, SymptomEntry


@admin.register(SymptomEntry)
class SymptomEntryAdmin(admin.ModelAdmin):
    list_display = ("user", "recorded_at", "category", "client_id", "created_at")
    list_filter = ("category",)
    search_fields = ("user__email", "client_id")


@admin.register(MoodEntry)
class MoodEntryAdmin(admin.ModelAdmin):
    list_display = ("user", "mood", "recorded_at", "client_id", "created_at")
    list_filter = ("mood",)
    search_fields = ("user__email", "client_id")
