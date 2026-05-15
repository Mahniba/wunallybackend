from django.conf import settings
from django.db import models


class Reminder(models.Model):
    ICON_CHOICES = [
        ("doctor", "Doctor"),
        ("vitamins", "Vitamins"),
        ("general", "General"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reminders",
    )
    title = models.CharField(max_length=200)
    time = models.CharField(max_length=64)
    completed = models.BooleanField(default=False)
    icon_type = models.CharField(max_length=20, choices=ICON_CHOICES, default="general", blank=True)
    client_id = models.CharField(max_length=64, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "client_id"],
                condition=models.Q(client_id__gt=""),
                name="unique_reminder_client_id_per_user",
            ),
        ]

    def __str__(self) -> str:
        return f"Reminder({self.user_id}, {self.title})"


class EmergencyContact(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="emergency_contacts",
    )
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=32)
    client_id = models.CharField(max_length=64, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "client_id"],
                condition=models.Q(client_id__gt=""),
                name="unique_contact_client_id_per_user",
            ),
        ]

    def __str__(self) -> str:
        return f"EmergencyContact({self.user_id}, {self.name})"


class CarePlanNotes(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="care_plan_notes",
    )
    medical = models.TextField(blank=True)
    labour_preferences = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"CarePlanNotes({self.user_id})"
