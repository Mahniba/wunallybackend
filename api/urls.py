from django.urls import path

from . import content_views, views

urlpatterns = [
    path("health/", views.health, name="health"),
    path("content/", content_views.app_content, name="app_content"),
]
