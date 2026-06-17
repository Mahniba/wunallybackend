from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .throttles import AuthRateThrottle
from .serializers import (
    AuthResponseSerializer,
    LoginSerializer,
    RegisterSerializer,
    UserSerializer,
)


def _auth_response(user) -> dict:
    refresh = RefreshToken.for_user(user)
    return {
        "user": UserSerializer(user).data,
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    }


class RegisterView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = [AuthRateThrottle]

    @extend_schema(
        tags=["Auth"],
        request=RegisterSerializer,
        responses={201: AuthResponseSerializer},
        auth=[],
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(_auth_response(user), status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = [AuthRateThrottle]

    @extend_schema(
        tags=["Auth"],
        request=LoginSerializer,
        responses={200: AuthResponseSerializer},
        auth=[],
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        return Response(_auth_response(user))


class PasswordResetView(APIView):
    """Research stub: always accepts request without revealing account existence."""

    permission_classes = [AllowAny]

    @extend_schema(
        tags=["Auth"],
        request={
            "application/json": {
                "type": "object",
                "properties": {"email": {"type": "string", "format": "email"}},
                "required": ["email"],
            }
        },
        responses={202: {"type": "object", "properties": {"detail": {"type": "string"}}}},
        auth=[],
    )
    def post(self, request):
        email = (request.data.get("email") or "").strip().lower()
        if not email:
            return Response({"email": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {
                "detail": (
                    "If an account exists for this email, password reset instructions "
                    "would be sent. (Research build — email not sent.)"
                )
            },
            status=status.HTTP_202_ACCEPTED,
        )


class LogoutView(APIView):
    @extend_schema(
        tags=["Auth"],
        request=None,
        responses={204: None},
        description=(
            "Discard tokens on the client. Optional refresh body for future blacklist support."
        ),
    )
    def post(self, request):
        return Response(status=status.HTTP_204_NO_CONTENT)
