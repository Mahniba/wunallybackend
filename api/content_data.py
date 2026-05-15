"""App content served to mobile clients (catalogs, navigation, copy)."""

CHECK_IN_CATEGORIES = [
    {
        "id": "mood",
        "title": "Mood & Feelings",
        "subtitle": "Track your emotions and mental well-being",
        "icon": "😊",
        "color_key": "chipTrack",
        "screen": "MoodCheckIn",
    },
    {
        "id": "general",
        "title": "General Symptoms",
        "subtitle": "Common symptoms you may be experiencing",
        "icon": "⚕️",
        "color_key": "chipReminders",
        "screen": "SymptomCheckIn",
        "symptom_category": "general",
        "show_extras": True,
    },
    {
        "id": "warning_signs",
        "title": "Warning Signs",
        "subtitle": "Important signs that need immediate attention",
        "icon": "⚠️",
        "color_key": "warning",
        "screen": "SymptomCheckIn",
        "symptom_category": "warning_signs",
    },
    {
        "id": "baby_monitoring",
        "title": "Baby Monitoring",
        "subtitle": "Track your baby's movements and well-being",
        "icon": "🤰",
        "color_key": "chipChat",
        "screen": "SymptomCheckIn",
        "symptom_category": "baby_monitoring",
    },
    {
        "id": "body_changes",
        "title": "Body Changes",
        "subtitle": "Normal changes during pregnancy",
        "icon": "🫙",
        "color_key": "chipTrack",
        "screen": "SymptomCheckIn",
        "symptom_category": "body_changes",
    },
    {
        "id": "vaginal_health",
        "title": "Vaginal Health",
        "subtitle": "Update about any discharge or related changes",
        "icon": "💧",
        "color_key": "chipReminders",
        "screen": "SymptomCheckIn",
        "symptom_category": "vaginal_health",
    },
]

SYMPTOM_CATALOGS = {
    "warning_signs": [
        {"key": "severe_headache", "label": "Severe headache", "emoji": "🤕"},
        {"key": "blurred_vision", "label": "Blurred vision", "emoji": "👁️"},
        {"key": "vaginal_bleeding", "label": "Vaginal bleeding", "emoji": "🩸"},
        {"key": "severe_abdominal_pain", "label": "Severe abdominal pain", "emoji": "🤢"},
        {"key": "nausea", "label": "Nausea", "emoji": "🤮"},
        {"key": "fever", "label": "Fever", "emoji": "🌡️"},
        {"key": "severe_vomiting", "label": "Severe vomiting", "emoji": "🤮"},
        {"key": "reduced_baby_movement", "label": "Reduced baby movement", "emoji": "👶"},
        {"key": "dizziness", "label": "Dizziness", "emoji": "🌀"},
        {"key": "insomnia", "label": "Insomnia", "emoji": "😴"},
        {"key": "foul_discharge", "label": "Foul-smelling discharge", "emoji": "🫗"},
        {"key": "difficulty_breathing", "label": "Difficulty breathing", "emoji": "😮‍💨"},
        {"key": "swelling_face_hands_feet", "label": "Swelling in face, hands or feet", "emoji": "✋"},
    ],
    "general": [
        {"key": "nausea", "label": "Nausea", "emoji": "🤮"},
        {"key": "headache", "label": "Headache", "emoji": "🤕"},
        {"key": "dizzy", "label": "Dizziness", "emoji": "🌀"},
        {"key": "fatigue", "label": "Fatigue", "emoji": "😴"},
        {"key": "back_pain", "label": "Back pain", "emoji": "🔙"},
    ],
    "baby_monitoring": [
        {"key": "reduced_baby_movement", "label": "Reduced movement", "emoji": "👶"},
        {"key": "strong_kicks", "label": "Strong kicks", "emoji": "🦶"},
        {"key": "irregular_pattern", "label": "Irregular pattern", "emoji": "📉"},
    ],
    "body_changes": [
        {"key": "swelling", "label": "Swelling", "emoji": "✋"},
        {"key": "heartburn", "label": "Heartburn", "emoji": "🔥"},
        {"key": "constipation", "label": "Constipation", "emoji": "🚽"},
        {"key": "stretch_marks", "label": "Stretch marks", "emoji": "〰️"},
    ],
    "vaginal_health": [
        {"key": "normal_discharge", "label": "Normal discharge", "emoji": "💧"},
        {"key": "unusual_discharge", "label": "Unusual discharge", "emoji": "⚠️"},
        {"key": "itching", "label": "Itching", "emoji": "🐜"},
        {"key": "odor", "label": "Unusual odor", "emoji": "👃"},
    ],
}

MOODS = [
    {"key": "happy", "label": "Happy", "emoji": "😊", "color_key": "moodHappy"},
    {"key": "ok", "label": "Okay", "emoji": "🙂", "color_key": "moodOk"},
    {"key": "tired", "label": "Tired", "emoji": "😴", "color_key": "moodTired"},
    {"key": "sleepy", "label": "Sleepy", "emoji": "💤", "color_key": "moodSleepy"},
    {"key": "confused", "label": "Confused", "emoji": "😕", "color_key": "moodConfused"},
    {"key": "sad", "label": "Sad", "emoji": "😢", "color_key": "moodSad"},
    {"key": "anxious", "label": "Anxious", "emoji": "😰", "color_key": "moodAnxious"},
    {"key": "stressed", "label": "Stressed", "emoji": "😣", "color_key": "moodStressed"},
]

HOME_ACTIONS = [
    {"key": "track", "title": "Track Progress", "nav": "Tracking", "color_key": "lavender"},
    {"key": "chat", "title": "Chat with AI", "nav": "Chat", "color_key": "chipChat"},
    {"key": "reminders", "title": "Reminders", "nav": "Reminders", "color_key": "chipReminders"},
    {"key": "sos", "title": "SOS Alert", "nav": "SOS", "color_key": "sos"},
]

CHAT_SUPPORT_OPTIONS = [
    {
        "key": "ai",
        "title": "Chat with AI",
        "description": "Get answers and tips anytime.",
        "icon": "💬",
        "screen": "Chat",
    },
    {
        "key": "nurse",
        "title": "Chat with Nurse",
        "description": "Connect with your care team (informational chat).",
        "icon": "👩‍⚕️",
        "screen": "Chat",
    },
    {
        "key": "voice",
        "title": "Talk to AI",
        "description": "Voice support when you need it.",
        "icon": "🎤",
        "screen": "Chat",
    },
]

CHAT_CONFIG = {
    "welcome_message": (
        "Hi! I'm here for general pregnancy support and tips. "
        "Ask me anything—this is not a substitute for medical care."
    ),
    "voice_prompts": [
        "I'd like some support.",
        "Can you give me a quick tip?",
        "How am I doing this week?",
    ],
    "input_placeholder": "Type your message...",
}
