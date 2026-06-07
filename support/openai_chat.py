"""OpenAI-backed supportive chat with safety guardrails (non-diagnostic)."""

from __future__ import annotations

from typing import Any

from decouple import config
from django.utils import timezone

from health.models import MoodEntry, SymptomEntry
from profiles.models import PregnancyProfile

from .chat_logic import DEFAULT_REPLY, DISCLAIMER, reply_for_message

WARNING_KEYS = frozenset({
    "severe_headache",
    "blurred_vision",
    "vaginal_bleeding",
    "severe_abdominal_pain",
    "fever",
    "severe_vomiting",
    "reduced_baby_movement",
    "dizziness",
    "difficulty_breathing",
    "swelling_face_hands_feet",
})

SYMPTOM_LABELS = {
    "severe_headache": "severe headache",
    "blurred_vision": "blurred vision",
    "vaginal_bleeding": "vaginal bleeding",
    "severe_abdominal_pain": "severe abdominal pain",
    "fever": "fever",
    "reduced_baby_movement": "reduced baby movement",
    "dizziness": "dizziness",
    "difficulty_breathing": "difficulty breathing",
    "swelling_face_hands_feet": "swelling (face, hands, or feet)",
}

AI_SYSTEM = """You are WunAlly, a pregnancy companion for women in Cameroon and similar low-resource settings.
You provide general, supportive, non-diagnostic information about nutrition, rest, sleep, emotional wellbeing, light activity, and common pregnancy concerns.
Rules:
- Never diagnose, prescribe medication, or replace a midwife, nurse, or doctor.
- Use simple, warm language. Prefer short paragraphs.
- If the user mentions danger signs (heavy bleeding, severe headache with vision changes, reduced fetal movement, severe pain, high fever, breathing difficulty, severe swelling with headache), urge them to contact their care provider or emergency services promptly.
- Encourage antenatal visits and following local clinic advice.
- Respond in the same language the user uses (English or French).
"""

NURSE_SYSTEM = """You are a registered midwife/nurse on WunAlly's Health Support Network in Cameroon.
Provide reassuring, non-diagnostic guidance, health education, and referral advice.
Do not diagnose or prescribe. Encourage clinic visits for concerning symptoms.
Use simple language. Match the user's language (English or French).
"""


def _recent_warning_signs(user) -> list[str]:
    since = timezone.now() - timezone.timedelta(days=7)
    found: list[str] = []
    for entry in SymptomEntry.objects.filter(user=user, recorded_at__gte=since).order_by("-recorded_at")[:20]:
        for key, active in (entry.symptoms or {}).items():
            if active and key in WARNING_KEYS and key not in found:
                found.append(key)
    return found


def build_user_context(user) -> str:
    parts: list[str] = []
    try:
        profile = user.pregnancy_profile
        parts.append(f"Gestational week (approx): {profile.weeks_pregnant}.")
        if profile.health_conditions.strip():
            parts.append(f"Health notes on file: {profile.health_conditions.strip()}.")
        if profile.age:
            parts.append(f"Age: {profile.age}.")
    except PregnancyProfile.DoesNotExist:
        pass

    warnings = _recent_warning_signs(user)
    if warnings:
        labels = ", ".join(SYMPTOM_LABELS.get(k, k) for k in warnings[:5])
        parts.append(f"Recent warning signs logged in app: {labels}.")

    mood = MoodEntry.objects.filter(user=user).order_by("-recorded_at").first()
    if mood:
        parts.append(f"Most recent mood check-in: {mood.mood}.")

    return " ".join(parts) if parts else "No profile context yet."


def _openai_client():
    from openai import OpenAI

    api_key = config("OPENAI_API_KEY", default="")
    if not api_key:
        return None
    return OpenAI(api_key=api_key)


def generate_chat_reply(
    user,
    text: str,
    *,
    mode: str = "ai",
    language: str = "en",
) -> dict[str, Any]:
    """Return {text, disclaimer, escalated, source}. Falls back to rules if no API key."""
    cleaned = (text or "").strip()
    if not cleaned:
        return {
            "text": DEFAULT_REPLY,
            "disclaimer": DISCLAIMER,
            "escalated": False,
            "source": "rules",
        }

    warnings = _recent_warning_signs(user)
    user_mentions_danger = any(
        label in cleaned.lower()
        for label in ["bleed", "saign", "vision", "movement", "fever", "fièvre", "breath", "souffle"]
    )
    escalated = bool(warnings) or user_mentions_danger

    client = _openai_client()
    if client is None:
        reply = reply_for_message(cleaned)
        if escalated:
            reply = (
                "Please contact your midwife, nurse, or clinic promptly about your symptoms. "
                + reply
            )
        return {
            "text": reply,
            "disclaimer": DISCLAIMER,
            "escalated": escalated,
            "source": "rules",
        }

    model = config("OPENAI_MODEL", default="gpt-4o-mini")
    max_tokens = config("CHAT_MAX_TOKENS", default=500, cast=int)
    system = NURSE_SYSTEM if mode == "nurse" else AI_SYSTEM
    lang_hint = "Reply in French." if language.startswith("fr") else "Reply in English."
    context = build_user_context(user)

    messages = [
        {"role": "system", "content": f"{system}\n{lang_hint}\nUser context: {context}"},
        {"role": "user", "content": cleaned},
    ]

    try:
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=0.4,
        )
        reply_text = (completion.choices[0].message.content or "").strip() or DEFAULT_REPLY
    except Exception:
        reply_text = reply_for_message(cleaned)

    if escalated and "provider" not in reply_text.lower() and "clinic" not in reply_text.lower():
        prefix = (
            "Important: seek care from your health provider if you are worried. "
            if not language.startswith("fr")
            else "Important : contactez votre prestataire de santé si vous êtes inquiète. "
        )
        reply_text = prefix + reply_text

    return {
        "text": reply_text,
        "disclaimer": DISCLAIMER,
        "escalated": escalated,
        "source": "openai",
    }
