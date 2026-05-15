from rest_framework import serializers

from .models import PregnancyProfile


class PregnancyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PregnancyProfile
        fields = (
            "name",
            "age",
            "weeks_pregnant",
            "due_date",
            "due_date_set",
            "health_conditions",
        )

    def validate_weeks_pregnant(self, value: int) -> int:
        if value < 1:
            return 1
        if value > 42:
            return 42
        return value
