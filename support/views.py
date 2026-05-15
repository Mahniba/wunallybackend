from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .chat_logic import DISCLAIMER, reply_for_message
from .models import AlertEvent, SOSEvent
from .serializers import (
    AlertEventCreateSerializer,
    AlertEventSerializer,
    ChatMessageSerializer,
    ChatResponseSerializer,
    SOSEventCreateSerializer,
    SOSEventSerializer,
)


@extend_schema_view(
    post=extend_schema(
        tags=["Support"],
        summary="Send chat message",
        operation_id="support_chat_send",
        request=ChatMessageSerializer,
        responses={200: ChatResponseSerializer},
        description="Informational support chat (not for diagnosis). Requires Bearer JWT.",
    ),
)
class ChatMessageView(APIView):
    def post(self, request):
        serializer = ChatMessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data["text"]
        return Response(
            {
                "text": reply_for_message(text),
                "disclaimer": DISCLAIMER,
            }
        )


class AlertEventListCreateView(generics.ListCreateAPIView):
    serializer_class = AlertEventSerializer

    def get_queryset(self):
        return AlertEvent.objects.filter(user=self.request.user)

    @extend_schema(tags=["Support"], summary="List symptom alert events")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Support"],
        summary="Log symptom alert event",
        request=AlertEventCreateSerializer,
    )
    def post(self, request, *args, **kwargs):
        body = AlertEventCreateSerializer(data=request.data)
        body.is_valid(raise_exception=True)
        event = AlertEvent.objects.create(user=request.user, **body.validated_data)
        return Response(AlertEventSerializer(event).data, status=status.HTTP_201_CREATED)


class SOSEventListCreateView(generics.ListCreateAPIView):
    serializer_class = SOSEventSerializer

    def get_queryset(self):
        return SOSEvent.objects.filter(user=self.request.user)

    @extend_schema(tags=["Support"], summary="List SOS events")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Support"],
        summary="Log SOS event",
        request=SOSEventCreateSerializer,
    )
    def post(self, request, *args, **kwargs):
        body = SOSEventCreateSerializer(data=request.data)
        body.is_valid(raise_exception=True)
        event = SOSEvent.objects.create(user=request.user, **body.validated_data)
        return Response(SOSEventSerializer(event).data, status=status.HTTP_201_CREATED)
