from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@extend_schema(
    tags=["System"],
    responses={
        200: {
            "type": "object",
            "properties": {
                "status": {"type": "string", "example": "ok"},
                "service": {"type": "string", "example": "wunally-api"},
                "version": {"type": "string", "example": "v1"},
            },
        }
    },
    auth=[],
)
@api_view(["GET"])
@permission_classes([AllowAny])
def health(request):
    """Public health check for mobile connectivity during development."""
    return Response(
        {
            "status": "ok",
            "service": "wunally-api",
            "version": "v1",
        }
    )
