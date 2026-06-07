from rest_framework import serializers

from .models import HealthFacility, HealthProvider, NurseAssignment


class HealthProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProvider
        fields = (
            "id",
            "name",
            "role",
            "facility",
            "phone",
            "languages",
            "avatar_emoji",
            "is_online",
            "last_seen",
            "bio",
        )


class NurseAssignmentSerializer(serializers.ModelSerializer):
    provider = HealthProviderSerializer(read_only=True)

    class Meta:
        model = NurseAssignment
        fields = ("id", "provider", "assigned_at", "active")


class AssignNurseSerializer(serializers.Serializer):
    provider_id = serializers.IntegerField()


class HealthFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthFacility
        fields = ("id", "name", "city", "region", "phone", "services")
