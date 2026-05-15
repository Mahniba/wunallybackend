from django.conf import settings
from django.db import models


class PregnancyProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="pregnancy_profile",
    )
    name = models.CharField(max_length=120, blank=True)
    age = models.CharField(max_length=10, blank=True)
    weeks_pregnant = models.PositiveSmallIntegerField(default=24)
    due_date = models.DateField(null=True, blank=True)
    due_date_set = models.BooleanField(default=False)
    health_conditions = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Profile({self.user.email})"
