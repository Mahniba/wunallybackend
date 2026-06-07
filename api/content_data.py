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

NETWORK_HUB = {
    "title_en": "Health Support Network",
    "title_fr": "Réseau de soutien santé",
    "subtitle_en": "Connect with nurses, AI support, and local care resources.",
    "subtitle_fr": "Connectez-vous aux infirmières, au soutien IA et aux ressources locales.",
}

NURSE_DIRECTORY = {
    "title_en": "Find a nurse",
    "title_fr": "Trouver une infirmière",
    "subtitle_en": "Available nurses appear on the nearest orbit. Tap one to connect.",
    "subtitle_fr": "Les infirmières disponibles apparaissent sur l'orbite la plus proche. Touchez pour vous connecter.",
    "scanning_en": "Searching for nurses…",
    "scanning_fr": "Recherche d'infirmières…",
    "hub_scanning_en": "Scanning",
    "hub_scanning_fr": "Recherche",
    "hub_you_en": "You",
    "hub_you_fr": "Vous",
    "found_online_en": "{count} nurse available",
    "found_online_plural_en": "{count} nurses available",
    "found_online_fr": "{count} infirmière disponible",
    "found_online_plural_fr": "{count} infirmières disponibles",
    "scan_again_en": "Scan again",
    "scan_again_fr": "Relancer la recherche",
    "more_nurses_en": "More available",
    "more_nurses_fr": "Autres disponibles",
    "empty_title_en": "No nurses on the network",
    "empty_title_fr": "Aucune infirmière sur le réseau",
    "empty_body_en": "No nurses are online right now. Try AI chat or scan again later.",
    "empty_body_fr": "Aucune infirmière en ligne pour le moment. Essayez le chat IA ou réessayez plus tard.",
    "status_offline_en": "No nurses online",
    "status_offline_fr": "Aucune infirmière en ligne",
    "online_en": "Online",
    "online_fr": "En ligne",
    "offline_en": "Offline",
    "offline_fr": "Hors ligne",
    "pick_nurse_en": "Start chat",
    "pick_nurse_fr": "Démarrer le chat",
    "languages_en": "Languages",
    "languages_fr": "Langues",
    "no_assignment_en": "No nurse assigned yet. Find one on the network.",
    "no_assignment_fr": "Aucune infirmière assignée. Trouvez-en une sur le réseau.",
}

FACILITIES_DIRECTORY = {
    "subtitle_en": "Hospitals and clinics from the pilot network list.",
    "subtitle_fr": "Hôpitaux et cliniques de la liste pilote du réseau.",
    "empty_title_en": "No facilities listed",
    "empty_title_fr": "Aucun établissement répertorié",
    "empty_body_en": "Facility data is not available right now. Try again later.",
    "empty_body_fr": "Les établissements ne sont pas disponibles pour le moment. Réessayez plus tard.",
    "services_en": "Services",
    "services_fr": "Services",
    "call_en": "Call",
    "call_fr": "Appeler",
}

NETWORK_HUB_FEATURES = [
    {
        "key": "find_nurse",
        "title_en": "Find a nurse now",
        "title_fr": "Trouver une infirmière",
        "description_en": "See who is online and choose support.",
        "description_fr": "Voir qui est en ligne et choisir un soutien.",
        "icon": "🔍",
        "screen": "NurseDirectory",
    },
    {
        "key": "nurse_chat",
        "title_en": "Chat with your nurse",
        "title_fr": "Discuter avec votre infirmière",
        "description_en": "Message your assigned midwife or nurse.",
        "description_fr": "Écrivez à votre sage-femme ou infirmière assignée.",
        "icon": "👩‍⚕️",
        "screen": "Chat",
        "params": {"mode": "nurse"},
    },
    {
        "key": "ai_chat",
        "title_en": "AI chat & voice",
        "title_fr": "Chat IA et vocal",
        "description_en": "Tips and support anytime (non-diagnostic).",
        "description_fr": "Conseils et soutien à tout moment (non diagnostique).",
        "icon": "💬",
        "screen": "Chat",
        "params": {"mode": "ai", "voice": True},
    },
    {
        "key": "facilities",
        "title_en": "Nearby facilities",
        "title_fr": "Établissements proches",
        "description_en": "Hospitals and clinics (pilot list).",
        "description_fr": "Hôpitaux et cliniques (liste pilote).",
        "icon": "🏥",
        "screen": "Facilities",
    },
    {
        "key": "danger_signs",
        "title_en": "Danger signs",
        "title_fr": "Signes de danger",
        "description_en": "Know when to seek care urgently.",
        "description_fr": "Savoir quand consulter en urgence.",
        "icon": "⚠️",
        "screen": "EmergencyGuide",
    },
    {
        "key": "warning_checkin",
        "title_en": "Log warning signs",
        "title_fr": "Enregistrer les signes d'alerte",
        "description_en": "Record symptoms from today's check-in.",
        "description_fr": "Noter les symptômes du suivi du jour.",
        "icon": "📋",
        "screen": "WarningSigns",
    },
]

REMINDER_PRESETS = [
    {"key": "anc", "title": "Antenatal clinic visit", "icon_type": "doctor"},
    {"key": "ultrasound", "title": "Ultrasound appointment", "icon_type": "doctor"},
    {"key": "iron", "title": "Take iron / folic acid", "icon_type": "vitamins"},
    {"key": "hydration", "title": "Drink water", "icon_type": "general"},
]

EMERGENCY_GUIDE = {
    "title": "Emergency steps (offline)",
    "disclaimer": "General guidance only — not medical diagnosis. Call emergency services or go to a facility when in danger.",
    "steps": [
        {
            "title": "Stay calm and get help",
            "body_en": "Ask someone nearby to stay with you. Use SOS to alert your contacts and share your location if possible.",
            "body_fr": "Demandez à une personne proche de rester avec vous. Utilisez SOS pour alerter vos contacts et partager votre position si possible.",
        },
        {
            "title": "Call or go to a facility",
            "body_en": "If you have heavy bleeding, severe pain, fits, fever, breathing difficulty, or reduced baby movement — go to a hospital or call emergency help immediately.",
            "body_fr": "Saignement important, douleur sévère, convulsions, fièvre, difficulté à respirer ou mouvements du bébé réduits — allez à l'hôpital ou appelez les urgences immédiatement.",
        },
        {
            "title": "While waiting for transport",
            "body_en": "Lie on your left side if faint. Do not eat or drink if vomiting severely or before surgery. Keep your clinic card and phone charged.",
            "body_fr": "Allongez-vous sur le côté gauche si vous vous sentez faible. Ne mangez pas si vomissements sévères. Gardez votre carnet de suivi et téléphone chargé.",
        },
    ],
    "danger_signs_en": [
        "Heavy vaginal bleeding",
        "Severe headache with blurred vision",
        "Severe abdominal pain",
        "Reduced or no baby movement (later pregnancy)",
        "High fever",
        "Difficulty breathing",
        "Fits / convulsions",
    ],
    "danger_signs_fr": [
        "Saignement vaginal abondant",
        "Mal de tête sévère avec vision trouble",
        "Douleur abdominale sévère",
        "Mouvements du bébé réduits ou absents",
        "Fièvre élevée",
        "Difficulté à respirer",
        "Convulsions",
    ],
    "sms_template_en": "SOS from WunAlly: I need urgent help during pregnancy. My location: {location}. Please call me or help me reach a hospital.",
    "sms_template_fr": "SOS WunAlly : j'ai besoin d'aide urgente pendant la grossesse. Ma position : {location}. Appelez-moi ou aidez-moi à rejoindre un hôpital.",
}
