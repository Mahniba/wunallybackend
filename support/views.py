from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AlertEvent, ChatMessage, SOSEvent
from .openai_chat import generate_chat_reply
from .serializers import (
    AlertEventCreateSerializer,
    AlertEventSerializer,
    ChatHistorySerializer,
    ChatMessageSerializer,
    ChatResponseSerializer,
    SOSEventCreateSerializer,
    SOSEventSerializer,
)


@extend_schema_view(
    post=extend_schema(
        tags=["Support"],
        summary="Send chat message (OpenAI with safety fallback)",
        operation_id="support_chat_send",
        request=ChatMessageSerializer,
        responses={200: ChatResponseSerializer},
    ),
    get=extend_schema(
        tags=["Support"],
        summary="List recent chat messages",
        responses={200: ChatHistorySerializer(many=True)},
    ),
)
class ChatMessageView(APIView):
    def get(self, request):
        mode = request.query_params.get("mode")
        qs = ChatMessage.objects.filter(user=request.user).order_by("-created_at")[:50]
        if mode in ("ai", "nurse"):
            qs = qs.filter(mode=mode)
        data = ChatHistorySerializer(reversed(list(qs)), many=True).data
        return Response(data)

    def post(self, request):
        serializer = ChatMessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        text = data["text"]
        mode = data.get("mode", "ai")
        input_mode = data.get("input_mode", "text")
        language = data.get("language", "en")
        provider_id = data.get("provider_id")

        ChatMessage.objects.create(
            user=request.user,
            role="user",
            text=text,
            mode=mode,
            input_mode=input_mode,
            provider_id=provider_id,
        )

        result = generate_chat_reply(
            request.user, text, mode=mode, language=language
        )

        ChatMessage.objects.create(
            user=request.user,
            role="assistant",
            text=result["text"],
            mode=mode,
            input_mode=input_mode,
            provider_id=provider_id,
            escalated=result.get("escalated", False),
            source=result.get("source", ""),
        )

        return Response(
            {
                "text": result["text"],
                "disclaimer": result["disclaimer"],
                "escalated": result.get("escalated", False),
                "source": result.get("source", ""),
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
        payload = body.validated_data
        event = SOSEvent.objects.create(user=request.user, **payload)
        return Response(SOSEventSerializer(event).data, status=status.HTTP_201_CREATED)
