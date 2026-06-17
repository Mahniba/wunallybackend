from django.utils.dateparse import parse_datetime
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MoodEntry, SymptomEntry
from .serializers import MoodEntrySerializer, SymptomEntrySerializer
from .tips_logic import build_personalized_tips


@extend_schema_view(
    get=extend_schema(
        tags=["Health"],
        description="List symptom entries for the authenticated user. Optional `from` and `to` ISO datetimes.",
    ),
    post=extend_schema(tags=["Health"]),
)
class SymptomListCreateView(generics.ListCreateAPIView):
    serializer_class = SymptomEntrySerializer

    def get_queryset(self):
        qs = SymptomEntry.objects.filter(user=self.request.user)
        from_param = self.request.query_params.get("from")
        to_param = self.request.query_params.get("to")
        if from_param:
            parsed = parse_datetime(from_param)
            if parsed:
                qs = qs.filter(recorded_at__gte=parsed)
        if to_param:
            parsed = parse_datetime(to_param)
            if parsed:
                qs = qs.filter(recorded_at__lte=parsed)
        return qs


@extend_schema_view(
    get=extend_schema(tags=["Health"], description="List mood entries for the authenticated user."),
    post=extend_schema(tags=["Health"]),
)
class MoodListCreateView(generics.ListCreateAPIView):
    serializer_class = MoodEntrySerializer

    def get_queryset(self):
        return MoodEntry.objects.filter(user=self.request.user)


class PersonalizedTipsView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Health"],
        description=(
            "Personalized tips from the user's profile, moods, and symptoms (last 14 days). "
            "Optional `week` query param overrides pregnancy week for context."
        ),
        responses={200: dict},
    )
    def get(self, request):
        week_param = request.query_params.get("week")
        week = None
        if week_param is not None:
            try:
                week = max(1, min(42, int(week_param)))
            except (TypeError, ValueError):
                week = None

        tips = build_personalized_tips(
            request.user,
            week=week,
            language=request.query_params.get("language", "en"),
        )
        resolved_week = week
        if resolved_week is None:
            try:
                resolved_week = request.user.pregnancy_profile.weeks_pregnant
            except Exception:
                resolved_week = 24

        return Response({"week": resolved_week, "tips": tips})
