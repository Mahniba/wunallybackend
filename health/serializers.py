from rest_framework import serializers

from .models import MoodEntry, SymptomEntry


class SymptomEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = SymptomEntry
        fields = (
            "id",
            "recorded_at",
            "category",
            "symptoms",
            "notes",
            "sleep_hours",
            "pain_level",
            "food_note",
            "client_id",
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        user = self.context["request"].user
        client_id = validated_data.get("client_id", "")
        if client_id:
            existing = SymptomEntry.objects.filter(user=user, client_id=client_id).first()
            if existing:
                for key, value in validated_data.items():
                    setattr(existing, key, value)
                existing.save()
                return existing
        validated_data["user"] = user
        return super().create(validated_data)


class MoodEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodEntry
        fields = ("id", "mood", "note", "recorded_at", "client_id")
        read_only_fields = ("id",)

    def validate_mood(self, value: str) -> str:
        valid = {choice[0] for choice in MoodEntry.MOOD_CHOICES}
        if value not in valid:
            raise serializers.ValidationError(f"Invalid mood. Choose one of: {', '.join(sorted(valid))}")
        return value

    def create(self, validated_data):
        user = self.context["request"].user
        client_id = validated_data.get("client_id", "")
        if client_id:
            existing = MoodEntry.objects.filter(user=user, client_id=client_id).first()
            if existing:
                for key, value in validated_data.items():
                    setattr(existing, key, value)
                existing.save()
                return existing
        validated_data["user"] = user
        return super().create(validated_data)
