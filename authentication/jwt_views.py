from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenRefreshView


class TokenRefreshResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField(required=False)


@extend_schema_view(
    post=extend_schema(
        tags=["Auth"],
        responses={200: TokenRefreshResponseSerializer},
        auth=[],
        description="Exchange a valid refresh token for a new access token.",
    ),
)
class DocumentedTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]
