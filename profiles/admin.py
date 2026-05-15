from django.contrib import admin

from .models import PregnancyProfile


@admin.register(PregnancyProfile)
class PregnancyProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "weeks_pregnant", "due_date", "updated_at")
    search_fields = ("user__email", "name")
