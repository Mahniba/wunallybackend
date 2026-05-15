from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CarePlanNotes, EmergencyContact, Reminder
from .serializers import (
    CarePlanNotesSerializer,
    EmergencyContactSerializer,
    ReminderSerializer,
)


@extend_schema_view(
    get=extend_schema(tags=["Care"]),
    post=extend_schema(tags=["Care"]),
)
class ReminderListCreateView(generics.ListCreateAPIView):
    serializer_class = ReminderSerializer

    def get_queryset(self):
        return Reminder.objects.filter(user=self.request.user)


@extend_schema_view(
    get=extend_schema(tags=["Care"]),
    patch=extend_schema(tags=["Care"]),
    put=extend_schema(tags=["Care"]),
    delete=extend_schema(tags=["Care"]),
)
class ReminderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReminderSerializer

    def get_queryset(self):
        return Reminder.objects.filter(user=self.request.user)


@extend_schema_view(
    get=extend_schema(tags=["Care"]),
    post=extend_schema(tags=["Care"]),
)
class ContactListCreateView(generics.ListCreateAPIView):
    serializer_class = EmergencyContactSerializer

    def get_queryset(self):
        return EmergencyContact.objects.filter(user=self.request.user)


@extend_schema_view(
    delete=extend_schema(tags=["Care"]),
)
class ContactDetailView(generics.DestroyAPIView):
    serializer_class = EmergencyContactSerializer

    def get_queryset(self):
        return EmergencyContact.objects.filter(user=self.request.user)


class CarePlanView(APIView):
    @extend_schema(
        tags=["Care"],
        responses={200: CarePlanNotesSerializer},
    )
    def get(self, request):
        notes, _created = CarePlanNotes.objects.get_or_create(user=request.user)
        return Response(CarePlanNotesSerializer(notes).data)

    @extend_schema(
        tags=["Care"],
        request=CarePlanNotesSerializer,
        responses={200: CarePlanNotesSerializer},
    )
    def patch(self, request):
        notes, _created = CarePlanNotes.objects.get_or_create(user=request.user)
        serializer = CarePlanNotesSerializer(notes, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
