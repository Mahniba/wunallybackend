"""App content served to mobile clients (catalogs, navigation, copy)."""

CHECK_IN_CATEGORIES = [
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
        {"key": "severe_headache", "label": "Severe headache", "emoji": "🤕", "description": "Very strong headache that does not ease with rest — especially with vision changes."},
        {"key": "blurred_vision", "label": "Blurred vision", "emoji": "👁️", "description": "Blurred vision, seeing spots, or light sensitivity — seek care right away."},
        {"key": "vaginal_bleeding", "label": "Vaginal bleeding", "emoji": "🩸", "description": "Any spotting or bleeding beyond light implantation — important to report."},
        {"key": "severe_abdominal_pain", "label": "Severe abdominal pain", "emoji": "🤢", "description": "Intense or sharp pain that doesn't feel like normal pregnancy discomfort."},
        {"key": "nausea", "label": "Nausea", "emoji": "🤮", "description": "Ongoing nausea that affects eating or drinking throughout the day."},
        {"key": "fever", "label": "Fever", "emoji": "🌡️", "description": "Temperature that feels higher than normal for you."},
        {"key": "severe_vomiting", "label": "Severe vomiting", "emoji": "🤮", "description": "Vomiting that prevents keeping fluids down."},
        {"key": "reduced_baby_movement", "label": "Reduced baby movement", "emoji": "👶", "description": "Noticeably fewer baby movements than you usually feel."},
        {"key": "dizziness", "label": "Dizziness", "emoji": "🌀", "description": "Feeling faint, weak, or unsteady at rest or when standing."},
        {"key": "insomnia", "label": "Insomnia", "emoji": "😴", "description": "Difficulty sleeping most nights despite feeling tired."},
        {"key": "foul_discharge", "label": "Foul-smelling discharge", "emoji": "🫗", "description": "Discharge with a strong unpleasant smell."},
        {"key": "difficulty_breathing", "label": "Difficulty breathing", "emoji": "😮‍💨", "description": "Shortness of breath at rest or with little activity."},
        {"key": "swelling_face_hands_feet", "label": "Swelling in face, hands or feet", "emoji": "✋", "description": "Rapid swelling of the face or hands — could be a sign of high blood pressure."},
    ],
    "general": [
        {"key": "nausea", "label": "Nausea", "emoji": "🤮", "description": "Feeling queasy or like you might vomit — very common especially in early pregnancy."},
        {"key": "headache", "label": "Headache", "emoji": "🤕", "description": "Throbbing or tension headaches, often linked to hormonal changes and blood flow."},
        {"key": "dizzy", "label": "Dizziness", "emoji": "🌀", "description": "Feeling lightheaded or faint, often from blood pressure changes or standing too fast."},
        {"key": "fatigue", "label": "Fatigue", "emoji": "😴", "description": "Feeling very tired or drained, even after resting — your body is working hard."},
        {"key": "back_pain", "label": "Back pain", "emoji": "🔙", "description": "Aching in the lower back as your posture shifts to support your growing belly."},
    ],
    "baby_monitoring": [
        {"key": "reduced_baby_movement", "label": "Reduced movement", "emoji": "👶", "description": "Baby feels less active than usual — worth tracking and mentioning to your midwife."},
        {"key": "strong_kicks", "label": "Strong kicks", "emoji": "🦶", "description": "You're feeling your baby move, kick, or roll — a reassuring daily sign."},
        {"key": "irregular_pattern", "label": "Irregular pattern", "emoji": "📉", "description": "Rhythmic fluttering or movement that feels different from your usual pattern."},
    ],
    "body_changes": [
        {"key": "swelling", "label": "Swelling", "emoji": "✋", "description": "Puffiness in hands, feet, or face from fluid retention and increased blood volume."},
        {"key": "heartburn", "label": "Heartburn", "emoji": "🔥", "description": "A burning feeling in the chest caused by stomach acid rising upward."},
        {"key": "constipation", "label": "Constipation", "emoji": "🚽", "description": "Difficulty with bowel movements caused by hormonal shifts and growing uterine pressure."},
        {"key": "stretch_marks", "label": "Stretch marks", "emoji": "〰️", "description": "Fine lines appearing on belly, hips, or breasts as skin stretches with growth."},
    ],
    "vaginal_health": [
        {"key": "normal_discharge", "label": "Normal discharge", "emoji": "💧", "description": "Clear or milky white discharge — healthy and normal throughout pregnancy."},
        {"key": "unusual_discharge", "label": "Unusual discharge", "emoji": "⚠️", "description": "Yellow, green, grey, or strong-smelling discharge — worth checking with your provider."},
        {"key": "itching", "label": "Itching", "emoji": "🐜", "description": "Discomfort, itching, or a burning sensation that may indicate irritation or infection."},
        {"key": "odor", "label": "Unusual odor", "emoji": "👃", "description": "A smell that is stronger or different than what is usual for you."},
    ],
}

MOODS = [
    {"key": "happy", "label": "Happy", "emoji": "😊", "color_key": "moodHappy", "description": "Feeling joyful, content, or excited about your pregnancy journey."},
    {"key": "ok", "label": "Okay", "emoji": "🙂", "color_key": "moodOk", "description": "Feeling steady and generally alright today — neither high nor low."},
    {"key": "tired", "label": "Tired", "emoji": "😴", "color_key": "moodTired", "description": "Low energy or needing more rest than usual."},
    {"key": "sleepy", "label": "Sleepy", "emoji": "💤", "color_key": "moodSleepy", "description": "Feeling drowsy or wanting to sleep more than usual."},
    {"key": "confused", "label": "Confused", "emoji": "😕", "color_key": "moodConfused", "description": "Feeling unsure, foggy, or having trouble focusing on things."},
    {"key": "sad", "label": "Sad", "emoji": "😢", "color_key": "moodSad", "description": "Feeling low, tearful, or emotionally drained — common during hormonal changes."},
    {"key": "anxious", "label": "Anxious", "emoji": "😰", "color_key": "moodAnxious", "description": "Feeling worried or uneasy about pregnancy, birth, or what lies ahead."},
    {"key": "stressed", "label": "Stressed", "emoji": "😣", "color_key": "moodStressed", "description": "Feeling easily frustrated or under pressure — a natural effect of big life changes."},
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
    "welcome_message_en": (
        "Hi! I'm here for general pregnancy support and tips. "
        "Ask me anything—this is not a substitute for medical care."
    ),
    "welcome_message_fr": (
        "Bonjour ! Je suis là pour un soutien général et des conseils sur la grossesse. "
        "Posez-moi vos questions — ceci ne remplace pas un avis médical."
    ),
    "voice_prompts_en": [
        "I'd like some support.",
        "Can you give me a quick tip?",
        "How am I doing this week?",
    ],
    "voice_prompts_fr": [
        "J'aimerais un peu de soutien.",
        "Pouvez-vous me donner un conseil rapide ?",
        "Comment je m'en sors cette semaine ?",
    ],
    "input_placeholder_en": "Type your message...",
    "input_placeholder_fr": "Écrivez votre message...",
    # Legacy keys for older clients
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
