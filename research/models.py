from django.conf import settings
from django.db import models


class StudyConsent(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="study_consent",
    )
    consented_at = models.DateTimeField(auto_now_add=True)
    consent_version = models.CharField(max_length=16, default="1.0")

    def __str__(self) -> str:
        return f"StudyConsent({self.user_id})"


class EvaluationResponse(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="evaluation_responses",
        null=True,
        blank=True,
    )
    participant_code = models.CharField(max_length=32, blank=True)
    instrument = models.CharField(max_length=32, default="sus")
    scores = models.JSONField(default=dict)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"EvaluationResponse({self.instrument}, {self.created_at})"
