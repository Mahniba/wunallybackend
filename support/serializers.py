from rest_framework import serializers

from .models import AlertEvent, SOSEvent


class ChatMessageSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=2000)


class ChatResponseSerializer(serializers.Serializer):
    text = serializers.CharField()
    disclaimer = serializers.CharField()


class AlertEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertEvent
        fields = ("id", "symptom", "count", "window_days", "message", "recorded_at")
        read_only_fields = ("id", "recorded_at")


class AlertEventCreateSerializer(serializers.Serializer):
    symptom = serializers.CharField(max_length=64)
    count = serializers.IntegerField(min_value=1)
    window_days = serializers.IntegerField(min_value=1)
    message = serializers.CharField()


class SOSEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SOSEvent
        fields = ("id", "recorded_at", "shared_location")
        read_only_fields = ("id", "recorded_at")


class SOSEventCreateSerializer(serializers.Serializer):
    shared_location = serializers.BooleanField(required=False, default=False)
