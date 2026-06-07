from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import HealthFacility, HealthProvider, NurseAssignment
from .serializers import (
    AssignNurseSerializer,
    HealthFacilitySerializer,
    HealthProviderSerializer,
    NurseAssignmentSerializer,
)


class ProviderListView(APIView):
    @extend_schema(tags=["Network"], summary="List health support providers")
    def get(self, request):
        online_only = request.query_params.get("online") == "1"
        qs = HealthProvider.objects.filter(active=True)
        if online_only:
            qs = qs.filter(is_online=True)
        return Response(HealthProviderSerializer(qs, many=True).data)


class FacilityListView(APIView):
    @extend_schema(tags=["Network"], summary="List local health facilities (pilot)")
    def get(self, request):
        qs = HealthFacility.objects.filter(active=True)
        return Response(HealthFacilitySerializer(qs, many=True).data)


class AssignProviderView(APIView):
    @extend_schema(
        tags=["Network"],
        summary="Assign selected nurse/midwife to current user",
        request=AssignNurseSerializer,
        responses={200: NurseAssignmentSerializer},
    )
    def post(self, request):
        body = AssignNurseSerializer(data=request.data)
        body.is_valid(raise_exception=True)
        provider = HealthProvider.objects.filter(
            active=True, id=body.validated_data["provider_id"]
        ).first()
        if not provider:
            return Response({"detail": "Provider not found."}, status=status.HTTP_404_NOT_FOUND)

        NurseAssignment.objects.filter(user=request.user, active=True).update(active=False)
        assignment = NurseAssignment.objects.create(
            user=request.user, provider=provider, active=True
        )
        return Response(NurseAssignmentSerializer(assignment).data)


class MyAssignmentView(APIView):
    @extend_schema(tags=["Network"], summary="Current nurse assignment")
    def get(self, request):
        assignment = (
            NurseAssignment.objects.filter(user=request.user, active=True)
            .select_related("provider")
            .first()
        )
        if not assignment:
            return Response(None)
        return Response(NurseAssignmentSerializer(assignment).data)
