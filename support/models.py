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
    """SOS activation log for research and safety review."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sos_events",
    )
    recorded_at = models.DateTimeField(auto_now_add=True)
    shared_location = models.BooleanField(default=False)
    contacts_notified_count = models.PositiveSmallIntegerField(default=0)
    sms_sent = models.BooleanField(default=False)
    offline_mode = models.BooleanField(default=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    class Meta:
        ordering = ["-recorded_at"]

    def __str__(self) -> str:
        return f"SOSEvent({self.user_id}, {self.recorded_at})"


class ChatMessage(models.Model):
    MODE_CHOICES = [("ai", "AI"), ("nurse", "Nurse")]
    ROLE_CHOICES = [("user", "User"), ("assistant", "Assistant")]
    INPUT_CHOICES = [("text", "Text"), ("voice", "Voice")]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="chat_messages",
    )
    role = models.CharField(max_length=16, choices=ROLE_CHOICES)
    text = models.TextField()
    mode = models.CharField(max_length=16, choices=MODE_CHOICES, default="ai")
    input_mode = models.CharField(max_length=16, choices=INPUT_CHOICES, default="text")
    provider_id = models.PositiveIntegerField(null=True, blank=True)
    escalated = models.BooleanField(default=False)
    source = models.CharField(max_length=16, default="openai", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self) -> str:
        return f"ChatMessage({self.user_id}, {self.role}, {self.mode})"
