from django.conf import settings
from django.db import models


class SymptomEntry(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="symptom_entries",
    )
    recorded_at = models.DateTimeField()
    category = models.CharField(max_length=32, default="warning_signs")
    symptoms = models.JSONField(default=dict)
    notes = models.TextField(blank=True)
    sleep_hours = models.FloatField(null=True, blank=True)
    pain_level = models.PositiveSmallIntegerField(null=True, blank=True)
    food_note = models.CharField(max_length=255, blank=True)
    client_id = models.CharField(max_length=64, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-recorded_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "client_id"],
                condition=models.Q(client_id__gt=""),
                name="unique_symptom_client_id_per_user",
            ),
        ]

    def __str__(self) -> str:
        return f"SymptomEntry({self.user_id}, {self.recorded_at})"


class MoodEntry(models.Model):
    MOOD_CHOICES = [
        ("tired", "Tired"),
        ("sleepy", "Sleepy"),
        ("confused", "Confused"),
        ("sad", "Sad"),
        ("anxious", "Anxious"),
        ("stressed", "Stressed"),
        ("happy", "Happy"),
        ("ok", "OK"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="mood_entries",
    )
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    note = models.TextField(blank=True)
    recorded_at = models.DateTimeField()
    client_id = models.CharField(max_length=64, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-recorded_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "client_id"],
                condition=models.Q(client_id__gt=""),
                name="unique_mood_client_id_per_user",
            ),
        ]

    def __str__(self) -> str:
        return f"MoodEntry({self.user_id}, {self.mood})"
