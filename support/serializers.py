from rest_framework import serializers

from .models import AlertEvent, ChatMessage, SOSEvent


class ChatMessageSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=2000)
    mode = serializers.ChoiceField(choices=["ai", "nurse"], default="ai")
    input_mode = serializers.ChoiceField(choices=["text", "voice"], default="text")
    language = serializers.CharField(max_length=8, required=False, default="en")
    provider_id = serializers.IntegerField(required=False, allow_null=True)


class ChatResponseSerializer(serializers.Serializer):
    text = serializers.CharField()
    disclaimer = serializers.CharField()
    escalated = serializers.BooleanField(required=False, default=False)
    source = serializers.CharField(required=False)


class ChatHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = (
            "id",
            "role",
            "text",
            "mode",
            "input_mode",
            "provider_id",
            "escalated",
            "created_at",
        )
        read_only_fields = fields


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
        fields = (
            "id",
            "recorded_at",
            "shared_location",
            "contacts_notified_count",
            "sms_sent",
            "offline_mode",
            "latitude",
            "longitude",
        )
        read_only_fields = ("id", "recorded_at")


class SOSEventCreateSerializer(serializers.Serializer):
    shared_location = serializers.BooleanField(required=False, default=False)
    contacts_notified_count = serializers.IntegerField(required=False, default=0, min_value=0)
    sms_sent = serializers.BooleanField(required=False, default=False)
    offline_mode = serializers.BooleanField(required=False, default=False)
    latitude = serializers.FloatField(required=False, allow_null=True)
    longitude = serializers.FloatField(required=False, allow_null=True)
