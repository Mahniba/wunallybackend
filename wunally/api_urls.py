"""API v1 URL router."""

from django.urls import include, path

urlpatterns = [
    path("", include("api.urls")),
    path("auth/", include("authentication.urls")),
    path("me/", include("profiles.urls")),
    path("me/", include("health.urls")),
    path("me/", include("care.urls")),
    path("me/", include("support.urls")),
    path("me/", include("network.urls")),
    path("me/", include("research.urls")),
]
