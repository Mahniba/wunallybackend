from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PregnancyProfile
from .serializers import PregnancyProfileSerializer


class ProfileView(APIView):
    @extend_schema(
        tags=["Profile"],
        responses={
            200: PregnancyProfileSerializer,
            404: OpenApiResponse(description="Profile not found."),
        },
    )
    def get(self, request):
        try:
            profile = request.user.pregnancy_profile
        except PregnancyProfile.DoesNotExist:
            return Response(
                {"detail": "Profile not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(PregnancyProfileSerializer(profile).data)

    @extend_schema(
        tags=["Profile"],
        request=PregnancyProfileSerializer,
        responses={200: PregnancyProfileSerializer},
        description="Create or update the authenticated user's pregnancy profile.",
    )
    def patch(self, request):
        profile, _created = PregnancyProfile.objects.get_or_create(user=request.user)
        serializer = PregnancyProfileSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
