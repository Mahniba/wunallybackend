# Wunally — Mobile Audit, Backend Plan & Integration Roadmap

**Document type:** Academic research planning  
**Last updated:** May 15, 2026  
**Repositories:** `wunally/` (Expo mobile) · `wunallybackend/` (Django)

---

## 1. Context & research framing

Wunally is a **maternal health companion mobile app** aimed at supporting pregnant users through check-ins, symptom awareness, reminders, emergency contacts, and educational content. This work sits in an **academic research** setting—not a production clinical product.

Implications for planning:

| Area | Research-oriented approach |
|------|----------------------------|
| **Scope** | Prioritize demonstrable end-to-end flows (auth → profile → symptom logging → retrieval) over full clinical certification |
| **Data** | Document consent, retention, and anonymization for study participants; separate dev/study databases |
| **Safety** | Rule-based alerts and SOS flows are **decision-support**, not diagnosis; state this clearly in UI and ethics materials |
| **Evaluation** | Backend enables centralized logging for study metrics (adherence, alert frequency) while respecting participant privacy |
| **Reproducibility** | Pin dependencies, document API contracts, and version mobile + backend together for paper/thesis artifacts |

---

## 2. Mobile app audit (`wunally/`)

### 2.1 Technology stack

| Layer | Choice |
|-------|--------|
| Framework | React Native via **Expo ~54** |
| Language | **TypeScript** |
| Navigation | React Navigation 7 (stack + bottom tabs) |
| State | **Zustand** stores with AsyncStorage / SecureStore persistence |
| UI | Custom theme (`colors`, `typography`, `spacing`), responsive hook |
| Charts | `react-native-chart-kit` + SVG |
| Device APIs | `expo-notifications`, `expo-location`, `expo-secure-store` |

**Not present today:** HTTP client layer, API base URL config, token refresh, offline sync queue, or any live backend calls.

### 2.2 Architecture (current)

```
App.tsx
  ├── Hydrates symptoms, schedules local notifications, evaluates rules → DoctorAlert
  └── NavigationContainer
        ├── RootNavigator (onboarding → auth → profile → main)
        ├── Sidebar (nutrition tips)
        └── DoctorAlert modal

Stores (Zustand)          Services (local only)
├── useAuthStore          ├── storage.ts (AsyncStorage keys)
├── useProfileStore       ├── notifications.ts
├── useSymptomsStore      ├── symptomRules.ts
├── useMoodStore          └── chat.ts (stub)
├── useRemindersStore
├── useContactsStore
└── useOnboardingStore
```

All user data is **device-local**. Auth is **mocked** (any email/password succeeds and writes to `@wunally/auth_user`).

### 2.3 Feature inventory

| Feature | Screens / components | Persistence | Backend-ready? |
|---------|---------------------|-------------|----------------|
| Onboarding | `OnboardingScreen` | `@wunally/onboarding_done` | Low priority (local OK) |
| Auth (login/signup/logout) | `LoginScreen`, `SignUpScreen`, etc. | `@wunally/auth_user` | **High** — `useAuthStore` has explicit TODOs |
| Email verification / forgot password | `VerificationScreen`, `ForgotPasswordScreen` | — | **High** — stubs only |
| User profile | `ProfileCreateScreen`, `ProfileScreen` | `@wunally/profile` | **High** |
| Dashboard & week tracking | `DashboardScreen`, `TrackingScreen`, `weekData.ts` | Profile-driven | Medium |
| Daily reminders | `RemindersScreen`, `useRemindersStore` | `@wunally/reminders` | Medium |
| Check-in hub | `CheckInHomeScreen` | — | Medium |
| Warning signs / symptoms | `WarningSignsScreen`, `SymptomsCheck`, chart | `@wunally/symptom_entries` | **High** (core research data) |
| Symptom rules & doctor alert | `symptomRules.ts`, `DoctorAlert` | Evaluated on device | Medium — could move server-side later |
| Symptom reminder time | `SymptomsSettings` | `@wunally/symptom_reminder_time` | Low (keep local scheduling) |
| Mood tracking | `MoodSummary`, `useMoodStore` | `@wunally/mood_entries` | **High** |
| Emergency contacts | `EmergencyContactsScreen`, SOS | `@wunally/emergency_contacts` | Medium |
| SOS + location share | `SOSScreen` | Contacts local; SMS/maps via device | Low for backend (optional audit log) |
| Chat / AI support | `ChatScreen`, `chat.ts`, `chatReplies.ts` | `@wunally/chat_history` key exists | Medium (future LLM API) |
| Care plan notes | `CarePlanNotesScreen` | `@wunally/care_plan_notes` | Medium |
| Health support / network | `HealthSupportScreen` | Static / local | Low |
| Privacy | `PrivacyScreen` | — | Content only |

### 2.4 Data models (mobile)

These types should drive Django models and API serializers.

**UserProfile** (`src/types/index.ts`)

```ts
{ name, age, weeksPregnant, dueDate, healthConditions, dueDateSet? }
```

**SymptomEntry** (`useSymptomsStore.ts`)

```ts
{ id, date (ISO), symptoms: Record<string, boolean>, notes?, sleepHours?, painLevel?, foodNote? }
```

Warning-sign keys (canonical list in `WarningSignsScreen.tsx`):  
`severe_headache`, `blurred_vision`, `vaginal_bleeding`, `severe_abdominal_pain`, `nausea`, `fever`, `severe_vomiting`, `reduced_baby_movement`, `dizziness`, `insomnia`, `foul_discharge`, `difficulty_breathing`, `swelling_face_hands_feet`.

Legacy/simple keys in `SymptomsCheck.tsx`: `nausea`, `headache`, `dizzy`.

**MoodEntry:** `{ id, mood: MoodType, timestamp, note? }` — moods: tired, sleepy, confused, sad, anxious, stressed, happy, ok.

**Reminder:** `{ id, title, time, completed, iconType? }`

**EmergencyContact:** `{ id, name, phone }`

**Auth user (mock):** `{ id, email, name }`

### 2.5 What works well (strengths)

- Clear navigation flow: onboarding → auth → profile creation → main tabs.
- Consistent theming and responsive layout patterns.
- Symptom pipeline is the most complete vertical slice: entry → persist → chart → rules → `DoctorAlert`.
- Storage abstraction (`storage.ts`, `STORAGE_KEYS`) makes backend migration straightforward.
- `expo-secure-store` is wired for tokens but unused—ready for JWT storage.
- Research-friendly documentation already exists (`README_SYMPTOMS.md`).

### 2.6 Gaps & technical debt

| Issue | Impact | Recommendation |
|-------|--------|----------------|
| No API layer | Blocks all server integration | Add `src/services/api/` + env-based `API_BASE_URL` |
| Mock authentication | No real users or security | Implement Django auth + JWT; wire `useAuthStore` |
| Duplicate symptom schemas | Warning signs vs `SymptomsCheck` use different keys | Normalize to one symptom catalog in backend + mobile constants |
| `CheckInHomeScreen` routes all categories to `WarningSigns` | Incomplete UX | Implement per-category screens or unified form with `category` field |
| `secureStorage` unused for tokens | Tokens would land in AsyncStorage if added carelessly | Store access/refresh tokens in SecureStore only |
| No sync / conflict handling | Data loss if user switches devices | Phase 2: last-write-wins or server-authoritative sync |
| No tests | Hard to validate research claims | Add unit tests for rules, stores, API client |
| Chat is placeholder | Misleading “AI” label in UI | Label as demo until backend/LLM connected |
| SOS does not notify backend | OK for MVP; optional event log for study | Optional `POST /sos-events/` (no PII in logs without consent) |

---

## 3. Backend audit (`wunallybackend/`)

### 3.1 Current state

| Component | Status |
|-----------|--------|
| Django **6.0.5** project `wunally` | Scaffolded |
| SQLite database | Default dev DB |
| App `authentication` | Empty `models.py`; stub `login` view returning plain text |
| URL | `GET /auth/login` → `"Hello, world..."` |
| REST framework | **Not installed** |
| CORS | **Not configured** |
| Custom user model | **Not defined** |
| Requirements file | **Missing** — add for reproducibility |

The backend is at **week zero**: suitable as a foundation, not yet an API.

### 3.2 Recommended backend stack (research MVP)

| Package / tool | Purpose |
|----------------|---------|
| `djangorestframework` | REST API |
| `djangorestframework-simplejwt` | Access + refresh tokens for mobile |
| `django-cors-headers` | Allow Expo dev client origins |
| `python-decouple` or `.env` | Secrets outside `settings.py` |
| `drf-spectacular` (optional) | OpenAPI docs for thesis appendix |
| PostgreSQL (later) | Study deployment; SQLite OK for local dev |

Keep **Django admin** enabled for researchers to inspect participant data (with role-based access in production study environment).

---

## 4. Proposed backend domain model

### 4.1 Django apps

```
wunallybackend/
├── authentication/     # User, registration, JWT, password reset
├── profiles/           # Pregnancy profile (1:1 with user)
├── health/             # SymptomEntry, MoodEntry, optional AlertEvent
├── reminders/          # User reminders (optional phase)
├── contacts/           # Emergency contacts (optional phase)
└── research/           # Study metadata, consent flags (optional)
```

### 4.2 Core models (sketch)

```python
# authentication
class User(AbstractUser):
    email = models.EmailField(unique=True)
    # phone optional for SMS research arm

# profiles
class PregnancyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    weeks_pregnant = models.PositiveSmallIntegerField(default=1)
    due_date = models.DateField(null=True, blank=True)
    health_conditions = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

# health
class SymptomEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recorded_at = models.DateTimeField()
    category = models.CharField(max_length=32, default='warning_signs')
    symptoms = models.JSONField()  # { "nausea": true, ... }
    notes = models.TextField(blank=True)
    sleep_hours = models.FloatField(null=True, blank=True)
    pain_level = models.PositiveSmallIntegerField(null=True, blank=True)
    food_note = models.CharField(max_length=255, blank=True)
    client_id = models.CharField(max_length=64, blank=True)  # idempotency / sync

class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=20)
    note = models.TextField(blank=True)
    recorded_at = models.DateTimeField()
```

Rule evaluation can remain on-device initially; optionally persist `AlertEvent` when rules fire for research analysis.

---

## 5. API contract (v1)

Base URL (dev): `http://<LAN-IP>:8000/api/v1/`  
Mobile reads from `EXPO_PUBLIC_API_URL` (Expo env).

### 5.1 Authentication

| Method | Endpoint | Body | Response |
|--------|----------|------|----------|
| POST | `/auth/register/` | `email`, `password`, `name` | `user`, `access`, `refresh` |
| POST | `/auth/login/` | `email`, `password` | `user`, `access`, `refresh` |
| POST | `/auth/token/refresh/` | `refresh` | `access` |
| POST | `/auth/logout/` | `refresh` | 204 (blacklist if enabled) |
| POST | `/auth/password/reset/` | `email` | 202 (stub OK for research) |
| POST | `/auth/verify/` | `code` | 200 (phase 2) |

### 5.2 Profile

| Method | Endpoint | Notes |
|--------|----------|-------|
| GET | `/me/profile/` | Returns pregnancy profile |
| PUT/PATCH | `/me/profile/` | Upsert from `ProfileCreateScreen` |

### 5.3 Health data

| Method | Endpoint | Notes |
|--------|----------|-------|
| GET | `/me/symptoms/` | Query `?from=&to=` for chart window |
| POST | `/me/symptoms/` | Create entry; accept `client_id` for dedup |
| GET | `/me/moods/` | List recent |
| POST | `/me/moods/` | Create mood entry |

### 5.4 Optional (phase 2+)

| Resource | Endpoints |
|----------|-----------|
| Reminders | CRUD `/me/reminders/` |
| Emergency contacts | CRUD `/me/contacts/` |
| Care plan notes | GET/PUT `/me/care-plan/` |
| Chat | POST `/me/chat/messages/` → proxied LLM or canned responses |
| Research | GET `/study/config/` consent version, feature flags |

### 5.5 Response shape (example)

```json
{
  "id": "uuid",
  "recorded_at": "2026-05-15T10:30:00Z",
  "symptoms": { "nausea": true, "severe_headache": false },
  "notes": "",
  "sleep_hours": 7,
  "pain_level": 2,
  "food_note": ""
}
```

---

## 6. Mobile ↔ backend integration plan

### Phase 0 — Project hygiene (1–2 days) ✅

**Backend**

- [x] Add `requirements.txt` (Django, DRF, simplejwt, cors-headers)
- [x] Split settings: `DEBUG`, `SECRET_KEY`, `ALLOWED_HOSTS`, `CORS_ALLOWED_ORIGINS` from environment
- [x] Register DRF + JWT + CORS in `settings.py`
- [x] Mount API at `/api/v1/` (health: `GET /api/v1/health/`)

**Mobile**

- [x] Add `EXPO_PUBLIC_API_URL` in `.env.example` / `app.config.js`
- [x] Create `src/services/api/client.ts` (fetch wrapper, auth header injection, 401 → refresh)
- [x] Create `src/services/api/auth.ts`, `profile.ts`, `symptoms.ts`, `moods.ts`

### Phase 1 — Authentication & profile (research MVP core) ✅

**Backend**

- [x] Custom user + register/login serializers
- [x] JWT issue on login/register; refresh endpoint
- [x] `PregnancyProfile` model + `/me/profile/`

**Mobile**

- [x] Replace mock logic in `useAuthStore.ts` with API calls
- [x] Persist `access`/`refresh` in `secureStorage`; user summary in AsyncStorage
- [x] On login success, fetch profile; route to `ProfileCreate` if 404/empty
- [x] `ProfileCreateScreen` → PATCH profile on save
- [x] Handle network errors with user-visible messages

**Definition of done:** New participant can register on phone, log in on a second session, and see the same profile.

### Phase 2 — Symptom & mood sync (primary research data) ✅

**Backend**

- [x] `SymptomEntry` + `MoodEntry` models, permissions (`IsAuthenticated`, object owner)
- [x] List + create endpoints with date filtering (`GET/POST /api/v1/me/symptoms/`, `GET/POST /api/v1/me/moods/`)

**Mobile**

- [x] On `addEntry` in `useSymptomsStore` / `useMoodStore`: POST to API, keep local copy on failure
- [x] On `hydrate`: merge server entries with local (union by `client_id`, server wins on duplicate)
- [x] `SymptomsChart` reads merged store (unchanged UI)
- [ ] Unify symptom key constants in `src/constants/symptoms.ts` (deferred)

**Definition of done:** Symptom logged on device appears in Django admin for that user; chart survives reinstall after login.

### Phase 3 — Reminders, contacts, care notes ✅

- [x] Backend CRUD for reminders and contacts (`/me/reminders/`, `/me/contacts/`, `/me/care-plan/`)
- [x] Wire `useRemindersStore`, `useContactsStore`, `useCarePlanStore`
- [x] Keep **local notification scheduling** on device; sync reminder definitions only

### Phase 4 — Chat, SOS logging, server-side rules (optional) ✅

- [x] Chat endpoint with safety disclaimers (`POST /api/v1/me/chat/messages/`)
- [x] `AlertEvent` logged when `evaluateSymptomRules` fires (`POST /api/v1/me/alerts/`)
- [x] SOS event timestamp logging (`POST /api/v1/me/sos-events/`, no coordinates stored)

### Phase 5 — Study hardening ✅ (dev-ready)

- [x] PostgreSQL optional via `DB_ENGINE=postgresql` in `.env`
- [x] API rate limiting (DRF throttles)
- [x] Participant export (`GET /api/v1/me/export/`)
- [x] Account deletion (`DELETE /api/v1/me/account/` + password)
- [x] Mobile: Privacy screen — export, delete, chat directions
- [ ] Production deploy (HTTPS, hosted DB) — manual for thesis deployment

---

## 7. Mobile integration touchpoints (file map)

| File | Change |
|------|--------|
| `src/store/useAuthStore.ts` | Replace mock with `authAPI` |
| `src/store/useProfileStore.ts` | `hydrate`/`persist` → GET/PATCH profile |
| `src/store/useSymptomsStore.ts` | POST on add; GET on hydrate |
| `src/store/useMoodStore.ts` | Same pattern |
| `src/services/storage.ts` | Keep for onboarding, notification time, offline cache |
| `src/services/chat.ts` | POST to backend |
| `App.tsx` | Optional: sync on foreground |
| New: `src/config/env.ts` | `API_BASE_URL` |

Suggested fetch wrapper behavior:

1. Attach `Authorization: Bearer <access>` when token exists.  
2. On 401, attempt refresh once, retry request.  
3. On network error, return structured error for UI.  
4. Never log passwords or tokens to console in study builds.

---

## 8. Research & ethics checklist

Document these in your IRB / ethics submission and link them to implementation:

- [ ] **Purpose limitation** — Collect only fields needed for study questions  
- [ ] **Informed consent** — Screen or flow before first sync (`PrivacyScreen` → consent flag on server)  
- [ ] **Data minimization** — SOS location shared only via user action, not background tracking  
- [ ] **Retention policy** — Auto-delete N months post-study  
- [ ] **Right to withdraw** — `DELETE /me/` cascades user data  
- [ ] **Non-diagnostic disclaimer** — Visible on check-in, chat, and alerts  
- [ ] **Security** — TLS, hashed passwords, JWT expiry, no secrets in mobile repo  

---

## 9. Suggested timeline (academic semester)

| Weeks | Milestone |
|-------|-----------|
| 1–2 | Phase 0 + Phase 1 (auth, profile, API skeleton) |
| 3–4 | Phase 2 (symptoms + moods sync, admin inspection) |
| 5 | Mobile polish: fix check-in routing, symptom key normalization |
| 6 | Phase 3 or pilot with small participant group |
| 7–8 | Evaluation metrics, export, thesis/write-up alignment |
| Optional | Phase 4–5 if scope allows |

---

## 10. Open decisions (resolve before coding Phase 1)

1. **Email as username?** Mobile already uses email login—recommend `USERNAME_FIELD = 'email'`.  
2. **Guest / offline-only mode?** Allow app use without account for demos, or require registration for study?  
3. **Single device vs multi-device?** Affects sync strategy.  
4. **Server-side rule engine?** Start client-side (already implemented); migrate if thesis needs centralized alerting.  
5. **Hosting** — University server vs cloud; drives HTTPS and CORS config.  
6. **Chat** — Real LLM (API cost, safety review) vs scripted replies for pilot?

---

## 11. Immediate next actions

| Priority | Owner | Task |
|----------|-------|------|
| P0 | Backend | `requirements.txt`, DRF, JWT, CORS, `/api/v1/` router |
| P0 | Backend | User model + register/login + profile endpoints |
| P0 | Mobile | API client + env URL + wire `useAuthStore` |
| P1 | Both | Symptom/mood models and sync |
| P1 | Mobile | `src/constants/symptoms.ts` shared catalog |
| P2 | Research | Consent flag + privacy copy aligned with IRB |

---

## Appendix A — Storage keys (mobile, pre-migration)

| Key | Content |
|-----|---------|
| `@wunally/auth_user` | Mock user JSON (replace with token + minimal cache) |
| `@wunally/profile` | `UserProfile` |
| `@wunally/symptom_entries` | `SymptomEntry[]` |
| `@wunally/mood_entries` | `MoodEntry[]` |
| `@wunally/reminders` | `Reminder[]` |
| `@wunally/emergency_contacts` | `EmergencyContact[]` |
| `@wunally/care_plan_notes` | string |
| `@wunally/onboarding_done` | `'true'` |
| `@wunally/symptom_reminder_time` | `HH:MM` |

---

## Appendix B — Reference: backend URL today

```
GET http://localhost:8000/auth/login  →  plain text stub
```

Target after Phase 1:

```
POST http://localhost:8000/api/v1/auth/login/
POST http://localhost:8000/api/v1/auth/register/
GET  http://localhost:8000/api/v1/me/profile/
```

---

*This document should be updated as phases complete. Tag mobile and backend repos with the same version label for thesis reproducibility (e.g. `study-pilot-v0.1`).*
