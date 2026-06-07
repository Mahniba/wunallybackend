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
from network.models import NurseAssignment
from profiles.models import PregnancyProfile
from profiles.serializers import PregnancyProfileSerializer
from support.models import AlertEvent, ChatMessage, SOSEvent
from support.serializers import AlertEventSerializer, SOSEventSerializer

from .models import EvaluationResponse, StudyConsent
from .serializers import (
    DeleteAccountSerializer,
    EvaluationResponseSerializer,
    StudyConsentSerializer,
)


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

        assignment = (
            NurseAssignment.objects.filter(user=user, active=True).select_related("provider").first()
        )

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
            "sos_events": SOSEventSerializer(
                SOSEvent.objects.filter(user=user), many=True
            ).data,
            "chat_messages": list(
                ChatMessage.objects.filter(user=user)
                .order_by("created_at")
                .values("role", "text", "mode", "created_at")
            ),
            "nurse_assignment": (
                {
                    "provider_id": assignment.provider_id,
                    "provider_name": assignment.provider.name,
                    "assigned_at": assignment.assigned_at.isoformat(),
                }
                if assignment
                else None
            ),
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


class StudyConsentView(APIView):
    @extend_schema(tags=["Research"], summary="Record study consent", responses={201: StudyConsentSerializer})
    def post(self, request):
        consent, _ = StudyConsent.objects.update_or_create(
            user=request.user,
            defaults={"consent_version": request.data.get("consent_version", "1.0")},
        )
        return Response(StudyConsentSerializer(consent).data, status=status.HTTP_201_CREATED)

    @extend_schema(tags=["Research"], summary="Get study consent status")
    def get(self, request):
        try:
            consent = request.user.study_consent
        except StudyConsent.DoesNotExist:
            return Response({"consented": False})
        return Response({"consented": True, **StudyConsentSerializer(consent).data})


class EvaluationSubmitView(APIView):
    @extend_schema(
        tags=["Research"],
        summary="Submit evaluation instrument (e.g. SUS)",
        request=EvaluationResponseSerializer,
    )
    def post(self, request):
        serializer = EvaluationResponseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        row = EvaluationResponse.objects.create(
            user=request.user,
            **serializer.validated_data,
        )
        return Response({"id": row.id, "instrument": row.instrument}, status=status.HTTP_201_CREATED)
