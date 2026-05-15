from rest_framework import serializers


class DeleteAccountSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
