from django.conf import settings
from django.db import models


class AlertEvent(models.Model):
    """Logged when symptom rules suggest contacting a provider."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="alert_events",
    )
    symptom = models.CharField(max_length=64)
    count = models.PositiveSmallIntegerField()
    window_days = models.PositiveSmallIntegerField()
    message = models.TextField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-recorded_at"]

    def __str__(self) -> str:
        return f"AlertEvent({self.user_id}, {self.symptom})"


class SOSEvent(models.Model):
    """Anonymized SOS tap for research adherence (no location stored by default)."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sos_events",
    )
    recorded_at = models.DateTimeField(auto_now_add=True)
    shared_location = models.BooleanField(default=False)

    class Meta:
        ordering = ["-recorded_at"]

    def __str__(self) -> str:
        return f"SOSEvent({self.user_id}, {self.recorded_at})"
