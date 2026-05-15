from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .content_data import (
    CHAT_CONFIG,
    CHAT_SUPPORT_OPTIONS,
    CHECK_IN_CATEGORIES,
    HOME_ACTIONS,
    MOODS,
    SYMPTOM_CATALOGS,
)


@extend_schema(
    tags=["Content"],
    responses={200: dict},
    auth=[],
)
@api_view(["GET"])
@permission_classes([AllowAny])
def app_content(request):
    """Bootstrap content for mobile: check-in categories, symptom catalogs, moods, home actions."""
    return Response(
        {
            "check_in_categories": CHECK_IN_CATEGORIES,
            "symptom_catalogs": SYMPTOM_CATALOGS,
            "moods": MOODS,
            "home_actions": HOME_ACTIONS,
            "chat": CHAT_CONFIG,
            "chat_support_options": CHAT_SUPPORT_OPTIONS,
        }
    )
