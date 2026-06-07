from django.contrib import admin

from .models import EvaluationResponse, StudyConsent


@admin.register(StudyConsent)
class StudyConsentAdmin(admin.ModelAdmin):
    list_display = ("user", "consented_at", "consent_version")


@admin.register(EvaluationResponse)
class EvaluationResponseAdmin(admin.ModelAdmin):
    list_display = ("instrument", "participant_code", "user", "created_at")
