from django.conf import settings
from django.db import models


class HealthProvider(models.Model):
    ROLE_CHOICES = [
        ("midwife", "Midwife"),
        ("nurse", "Nurse"),
    ]

    name = models.CharField(max_length=120)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="nurse")
    facility = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=32, blank=True)
    languages = models.JSONField(default=list, blank=True)
    avatar_emoji = models.CharField(max_length=8, default="👩‍⚕️")
    is_online = models.BooleanField(default=False)
    last_seen = models.DateTimeField(auto_now=True)
    bio = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-is_online", "name"]

    def __str__(self) -> str:
        return f"{self.name} ({self.role})"


class NurseAssignment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="nurse_assignments",
    )
    provider = models.ForeignKey(
        HealthProvider,
        on_delete=models.CASCADE,
        related_name="assignments",
    )
    assigned_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-assigned_at"]

    def __str__(self) -> str:
        return f"Assignment({self.user_id} -> {self.provider_id})"


class HealthFacility(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=80, default="Douala")
    region = models.CharField(max_length=80, default="Littoral")
    phone = models.CharField(max_length=32, blank=True)
    services = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
