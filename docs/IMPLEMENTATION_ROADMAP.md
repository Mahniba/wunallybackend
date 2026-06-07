# WunAlly Implementation Roadmap

**Status:** Phases 0–6 implemented in codebase (May 2026).  
**Repos:** `wunally/` (Expo) · `wunallybackend/` (Django)

## Completed

| Phase | Scope | Key paths |
|-------|--------|-----------|
| 0 | Thesis alignment notes | `docs/THESIS_ALIGNMENT_EDITS.md` |
| 1 | EN/FR i18n, offline emergency copy | `src/i18n/`, `src/assets/offlineEmergency.ts`, `api/content_data.py` |
| 2 | OpenAI chat (server proxy) | `support/openai_chat.py`, `POST /me/chat/messages/` |
| 3 | Voice STT → API → TTS | `src/services/voice.ts`, `expo-speech`, `expo-speech-recognition` |
| 4 | Health Support Network hub | `HealthSupportScreen`, `NurseDirectoryScreen`, `network/` app |
| 5 | SOS SMS + location + offline guide | `src/services/sosAlerts.ts`, `SOSScreen`, `EmergencyGuideScreen` |
| 6 | Study consent + SUS | `StudyConsentScreen`, `SUSQuestionnaireScreen`, `research/` models |
| 7 | Tracking polish (no weight/BP) | Care plan allergies, reminder presets |

## Setup

### Backend

```bash
cd wunallybackend
cp .env.example .env
# Set OPENAI_API_KEY=sk-...
./venv/bin/pip install -r requirements.txt
./venv/bin/python manage.py migrate
./venv/bin/python manage.py seed_network
./venv/bin/python manage.py runserver 0.0.0.0:8000
```

### Mobile

```bash
cd wunally
npm install
# EXPO_PUBLIC_API_URL=http://<LAN-IP>:8000/api/v1 in .env
npm run start
```

## Thesis writing split

- **Chapter 3.6:** What was *designed and implemented* (features above).
- **Chapter 3.7 / 4:** What was *evaluated* with participants (run SUS + task sessions; results are not automatic from the build).

## Optional next steps

- Production HTTPS + PostgreSQL (`DB_ENGINE=postgresql`)
- Real nurse dashboard (replace seeded online status)
- French translations for all API-driven content strings
- Clinical safety review log export for midwife reviewers
