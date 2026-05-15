"""Personalized informational tips from profile + recent health data (not clinical advice)."""

from __future__ import annotations

from collections import Counter
from datetime import timedelta
from typing import Any

from django.utils import timezone

from api.content_data import SYMPTOM_CATALOGS
from profiles.models import PregnancyProfile

from .models import MoodEntry, SymptomEntry

SYMPTOM_LABELS: dict[str, str] = {}
for _items in SYMPTOM_CATALOGS.values():
    for _item in _items:
        SYMPTOM_LABELS[_item["key"]] = _item["label"]

WARNING_KEYS = {s["key"] for s in SYMPTOM_CATALOGS.get("warning_signs", [])}

MOOD_SUPPORT: dict[str, tuple[str, str]] = {
    "anxious": (
        "Stress support (quick reset)",
        "Try 4–6 slow breaths and a short walk if you can. If worry feels intense, "
        "consider reaching out to your provider or support person today.",
    ),
    "stressed": (
        "Stress support (quick reset)",
        "Try 4–6 slow breaths and a short walk if you can. If worry feels intense, "
        "consider reaching out to your provider or support person today.",
    ),
    "sad": (
        "Gentle check-in",
        "You've logged a low mood recently. Small steps help: message a friend, "
        "rest, and hydrate. If sadness is persistent, your provider can help.",
    ),
    "tired": (
        "Energy & sleep",
        "Plan one rest block today. Side-sleeping with a pillow between knees may help.",
    ),
    "sleepy": (
        "Energy & sleep",
        "Plan one rest block today. Side-sleeping with a pillow between knees may help.",
    ),
    "happy": (
        "Keep the momentum",
        "You're tracking positive mood — great. Keep hydration and gentle movement in your routine.",
    ),
    "ok": (
        "Steady week",
        "Your mood looks steady. Small habits (water, short walks, regular meals) add up.",
    ),
}

SYMPTOM_GUIDANCE: dict[str, str] = {
    "nausea": "Try smaller meals and ginger if it helps. If you can't keep fluids down, contact your provider.",
    "headache": "Hydration and regular meals often help. Severe or sudden headaches with vision changes need urgent care.",
    "dizzy": "Sit and stand slowly, hydrate, and eat regularly. Frequent dizziness or fainting needs a provider call.",
    "dizziness": "Sit and stand slowly, hydrate, and eat regularly. Frequent dizziness or fainting needs a provider call.",
    "severe_headache": "Severe headaches in pregnancy should be evaluated — contact your provider, especially with vision changes.",
    "vaginal_bleeding": "Any bleeding should be reported to your provider promptly.",
    "reduced_baby_movement": "If baby's movements feel reduced, contact your provider today for guidance.",
    "fever": "Fever in pregnancy should be checked — contact your provider for safe next steps.",
    "swelling_face_hands_feet": "Sudden swelling with headache or vision changes can be urgent — call your provider.",
}


def _week_band_tip(week: int) -> dict[str, str]:
    if week <= 13:
        return {
            "title": f"First trimester focus (Week {week})",
            "body": "Folate, rest when tired, and small frequent meals if nauseous. Book or keep your prenatal visits.",
            "source": "week",
        }
    if week <= 27:
        return {
            "title": f"Second trimester focus (Week {week})",
            "body": "Many feel more energy now — stay active gently, eat iron-rich foods, and note baby movements as they begin.",
            "source": "week",
        }
    return {
        "title": f"Third trimester focus (Week {week})",
        "body": "Rest when needed, sleep on your side if comfortable, and know your warning signs. Keep prenatal appointments.",
        "source": "week",
    }


def build_personalized_tips(user, week: int | None = None) -> list[dict[str, Any]]:
    tips: list[dict[str, Any]] = []
    seen_titles: set[str] = set()

    def add(title: str, body: str, source: str) -> None:
        if title in seen_titles:
            return
        seen_titles.add(title)
        tips.append({"title": title, "body": body, "source": source})

    profile: PregnancyProfile | None = PregnancyProfile.objects.filter(user=user).first()

    resolved_week = week if week is not None else (profile.weeks_pregnant if profile else 24)
    resolved_week = max(1, min(42, int(resolved_week)))

    since_14 = timezone.now() - timedelta(days=14)
    since_7 = timezone.now() - timedelta(days=7)

    moods = list(MoodEntry.objects.filter(user=user, recorded_at__gte=since_14).order_by("-recorded_at"))
    symptoms = list(SymptomEntry.objects.filter(user=user, recorded_at__gte=since_14))

    # --- Moods ---
    if moods:
        latest = moods[0]
        if latest.mood in MOOD_SUPPORT:
            title, body = MOOD_SUPPORT[latest.mood]
            add(title, body, "mood")
        mood_counts = Counter(m.mood for m in moods if m.recorded_at >= since_7)
        if mood_counts.get("anxious", 0) + mood_counts.get("stressed", 0) >= 3:
            add(
                "Frequent stress this week",
                "You've logged stress or anxiety several times. Consider a support person, "
                "breathing breaks, and discussing patterns with your provider if it continues.",
                "mood",
            )

    # --- Symptoms (all keys) ---
    symptom_counts: Counter[str] = Counter()
    warning_recent: list[str] = []
    sleep_vals: list[float] = []
    pain_vals: list[int] = []

    for entry in symptoms:
        recorded = entry.recorded_at
        for key, active in (entry.symptoms or {}).items():
            if not active:
                continue
            symptom_counts[key] += 1
            if recorded >= since_7 and key in WARNING_KEYS:
                warning_recent.append(key)

        if entry.sleep_hours is not None:
            sleep_vals.append(float(entry.sleep_hours))
        if entry.pain_level is not None:
            pain_vals.append(int(entry.pain_level))

    if warning_recent:
        unique_warn = sorted(set(warning_recent), key=warning_recent.index)
        labels = ", ".join(SYMPTOM_LABELS.get(k, k.replace("_", " ")) for k in unique_warn[:3])
        add(
            "Important symptoms logged",
            f"You recently noted: {labels}. These can need prompt attention — "
            "contact your care provider if you are concerned or symptoms worsen.",
            "warning",
        )

    if symptom_counts:
        top_key, top_count = symptom_counts.most_common(1)[0]
        label = SYMPTOM_LABELS.get(top_key, top_key.replace("_", " "))
        guidance = SYMPTOM_GUIDANCE.get(
            top_key,
            f"You've tracked {label.lower()} {top_count} time(s) recently. "
            "Monitor changes and discuss persistent symptoms with your provider.",
        )
        add(f"Symptom focus: {label}", guidance, "symptom")

    if sleep_vals:
        avg_sleep = sum(sleep_vals) / len(sleep_vals)
        if avg_sleep < 6.5:
            add(
                "Sleep target",
                f"Your recent sleep average is about {avg_sleep:.1f}h. "
                "Try a consistent bedtime, side-sleeping, and a short wind-down without screens.",
                "sleep",
            )

    if pain_vals:
        avg_pain = sum(pain_vals) / len(pain_vals)
        if avg_pain >= 5:
            add(
                "Pain plan",
                f"Your recent pain average is about {avg_pain:.1f}/10. "
                "Gentle movement and position changes may help. Severe or worsening pain needs a provider call.",
                "pain",
            )

    # --- Profile ---
    if profile:
        if profile.health_conditions.strip():
            add(
                "Your health note",
                f'You noted: "{profile.health_conditions.strip()}". '
                "Bring questions about this to your next appointment.",
                "profile",
            )
        try:
            age = int(profile.age)
            if age >= 35:
                add(
                    "Appointments & monitoring",
                    "If you're 35+, your provider may recommend extra monitoring. "
                    "Keep appointments and ask which warning signs should prompt a call.",
                    "profile",
                )
        except (TypeError, ValueError):
            pass

    # --- Week context (always include one band tip) ---
    band = _week_band_tip(resolved_week)
    add(band["title"], band["body"], band["source"])

    return tips[:8]
