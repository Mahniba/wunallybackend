from rest_framework import serializers

from .models import CarePlanNotes, EmergencyContact, Reminder


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = (
            "id",
            "title",
            "time",
            "completed",
            "icon_type",
            "client_id",
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        user = self.context["request"].user
        client_id = validated_data.get("client_id", "")
        if client_id:
            existing = Reminder.objects.filter(user=user, client_id=client_id).first()
            if existing:
                for key, value in validated_data.items():
                    setattr(existing, key, value)
                existing.save()
                return existing
        validated_data["user"] = user
        return super().create(validated_data)


class EmergencyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyContact
        fields = ("id", "name", "phone", "client_id")
        read_only_fields = ("id",)

    def create(self, validated_data):
        user = self.context["request"].user
        client_id = validated_data.get("client_id", "")
        if client_id:
            existing = EmergencyContact.objects.filter(user=user, client_id=client_id).first()
            if existing:
                for key, value in validated_data.items():
                    setattr(existing, key, value)
                existing.save()
                return existing
        validated_data["user"] = user
        return super().create(validated_data)


class CarePlanNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarePlanNotes
        fields = ("medical", "labour_preferences", "updated_at")
        read_only_fields = ("updated_at",)
