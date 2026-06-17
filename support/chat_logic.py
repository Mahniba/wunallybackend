"""Rule-based informational replies (not clinical diagnosis)."""

CHAT_REPLIES = [
    (["eat", "food", "diet", "nutrition", "meal", "hungry"],
     "Focus on iron-rich foods like spinach, beans, and lean meat. Small, frequent meals can help with nausea. Stay hydrated."),
    (["pain", "hurt", "ache", "cramp", "uncomfortable"],
     "Some discomfort is common in pregnancy. If pain is severe or persistent, contact your care provider."),
    (["sleep", "tired", "rest", "exhausted"],
     "Rest when you can. Sleeping on your left side in later pregnancy can help."),
    (["nausea", "sick", "vomit", "morning sickness"],
     "Nausea is common. Small, bland snacks can help. If you cannot keep fluids down, see your provider."),
    (["stress", "anxious", "worry", "nervous"],
     "It is normal to feel worried sometimes. If anxiety affects daily life, your provider can suggest support."),
    (["bleed", "bleeding", "spotting", "saign", "saignement"],
     "Any bleeding in pregnancy should be checked. Contact your care provider promptly."),
    (["manger", "repas", "nutrition", "faim", "nourriture"],
     "Focus on iron-rich foods like spinach, beans, and lean meat. Small, frequent meals can help with nausea. Stay hydrated."),
    (["douleur", "mal", "crampes"],
     "Some discomfort is common in pregnancy. If pain is severe or persistent, contact your care provider."),
    (["dormir", "fatigue", "repos", "épuisée"],
     "Rest when you can. Sleeping on your left side in later pregnancy can help."),
    (["nausée", "vomir", "malade"],
     "Nausea is common. Small, bland snacks can help. If you cannot keep fluids down, see your provider."),
    (["stress", "anxieux", "inquiet", "inquiète", "nerveux"],
     "It is normal to feel worried sometimes. If anxiety affects daily life, your provider can suggest support."),
]

DEFAULT_REPLY = (
    "Thanks for your message. This chat offers general support only—not diagnosis. "
    "For personal medical advice, please contact your care provider."
)

DISCLAIMER = (
    "This response is for general information only and is not medical advice. "
    "Contact your care provider for personal guidance."
)


def reply_for_message(text: str) -> str:
    lower = text.lower().strip()
    for keywords, reply in CHAT_REPLIES:
        if any(k in lower for k in keywords):
            return reply
    return DEFAULT_REPLY
