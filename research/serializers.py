from rest_framework import serializers

from .models import EvaluationResponse, StudyConsent


class DeleteAccountSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)


class StudyConsentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyConsent
        fields = ("consented_at", "consent_version")
        read_only_fields = fields


class EvaluationResponseSerializer(serializers.Serializer):
    instrument = serializers.CharField(max_length=32, default="sus")
    participant_code = serializers.CharField(max_length=32, required=False, allow_blank=True)
    scores = serializers.JSONField()
    notes = serializers.CharField(required=False, allow_blank=True)
