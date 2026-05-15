from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from care.models import CarePlanNotes, EmergencyContact, Reminder
from care.serializers import CarePlanNotesSerializer, EmergencyContactSerializer, ReminderSerializer
from health.models import MoodEntry, SymptomEntry
from health.serializers import MoodEntrySerializer, SymptomEntrySerializer
from profiles.models import PregnancyProfile
from profiles.serializers import PregnancyProfileSerializer
from support.models import AlertEvent, SOSEvent
from support.serializers import AlertEventSerializer, SOSEventSerializer

from .serializers import DeleteAccountSerializer


class ExportDataView(APIView):
    @extend_schema(
        tags=["Research"],
        summary="Export my study data (JSON)",
        description="Download all data linked to the authenticated user for research or portability.",
    )
    def get(self, request):
        user = request.user
        profile = None
        try:
            profile = PregnancyProfileSerializer(user.pregnancy_profile).data
        except PregnancyProfile.DoesNotExist:
            profile = None

        care_plan = None
        try:
            care_plan = CarePlanNotesSerializer(user.care_plan_notes).data
        except CarePlanNotes.DoesNotExist:
            care_plan = {"medical": "", "labour_preferences": ""}

        payload = {
            "user": {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "date_joined": user.date_joined.isoformat(),
            },
            "profile": profile,
            "care_plan": care_plan,
            "symptoms": SymptomEntrySerializer(
                SymptomEntry.objects.filter(user=user), many=True
            ).data,
            "moods": MoodEntrySerializer(MoodEntry.objects.filter(user=user), many=True).data,
            "reminders": ReminderSerializer(Reminder.objects.filter(user=user), many=True).data,
            "emergency_contacts": EmergencyContactSerializer(
                EmergencyContact.objects.filter(user=user), many=True
            ).data,
            "alert_events": AlertEventSerializer(
                AlertEvent.objects.filter(user=user), many=True
            ).data,
            "sos_events": SOSEventSerializer(SOSEvent.objects.filter(user=user), many=True).data,
        }
        return Response(payload)


class DeleteAccountView(APIView):
    @extend_schema(
        tags=["Research"],
        summary="Delete my account and all data",
        request=DeleteAccountSerializer,
        responses={204: None},
    )
    def delete(self, request):
        serializer = DeleteAccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            email=request.user.email,
            password=serializer.validated_data["password"],
        )
        if user is None or user.id != request.user.id:
            raise ValidationError({"password": "Incorrect password."})
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
