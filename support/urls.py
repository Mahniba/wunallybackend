from django.urls import path

from .views import AlertEventListCreateView, ChatMessageView, SOSEventListCreateView

urlpatterns = [
    path("chat/messages/", ChatMessageView.as_view(), name="me-chat"),
    path("alerts/", AlertEventListCreateView.as_view(), name="me-alerts"),
    path("sos-events/", SOSEventListCreateView.as_view(), name="me-sos-events"),
]
