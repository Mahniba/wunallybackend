# Thesis alignment edits (paste into Wunally.docx)

Use these replacements so Chapter 1–3 match the implemented system (no weight/BP logs; Cameroon/low-resource features; evaluation separated from build).

---

## 1.3.1 Main research question — how to answer it

**Development (Ch. 3–4):** WunAlly was developed using user-centred, mobile-first design for **low-resource settings, with Cameroon as the primary design context**. The implementation combines pregnancy tracking (gestational week, trimesters, symptoms, mood, reminders, care-plan allergies), **OpenAI-assisted** non-diagnostic chat with safety prompts, a **voice interaction loop** (on-device speech recognition → server-mediated model → text-to-speech), a **Health Support Network** (online nurse directory, nurse chat mode, facility list, danger-sign content), and an **SOS module** (hold-to-alert, SMS to emergency contacts, location sharing, offline emergency steps), with **English and French** UI strings.

**Evaluation (Ch. 3.7 / results):** Usability, accessibility, perceived usefulness, privacy, and suitability for users with varying literacy and socio-economic backgrounds were assessed **separately** through SUS, task observation, and interviews—not conflated with the development description.

---

## 1.4.2 Objective 1 — replace

**Old:** …weight, blood pressure, allergies…

**New:** To design and implement a secure pregnancy tracking module for recording gestational age, trimester milestones, allergies and health conditions (care plan), symptoms, mood, reminders, appointments, and other relevant maternal health information.

---

## 1.3.2 SRQ 1 — align list

Remove weight and blood pressure. Keep: gestational age, trimester milestones, allergies (care plan), symptoms, reminders, antenatal adherence.

---

## 3.4.1 Functional requirements — remove

- Weight / blood pressure logging tables and screens
- `HealthRecords` table with `weight_kg`, `blood_pressure_*` in ERD

**Add:** OpenAI chat via secure backend; voice pipeline; network hub; SOS SMS; offline emergency guide; bilingual UI.

---

## 3.6.2 — AI module (accurate wording)

The AI module uses the **OpenAI API through a Django backend proxy** (API key never stored on the device). A system prompt enforces non-diagnostic, referral-oriented responses. User context includes gestational week, recent warning signs, mood, and care-plan notes. **Keyword-based fallback** applies when the API is unavailable.

Voice: **on-device speech recognition** (`expo-speech-recognition`) sends transcript to the same endpoint; replies can be read aloud with **expo-speech**.

---

## 3.6.3 — SOS module (accurate wording)

SOS uses **hold-to-activate** (2 seconds) to reduce false triggers. The app sends **SMS to all stored emergency contacts** with a bilingual template and optional Google Maps link from a one-shot GPS read. Users can **call the first contact**, **share location** via the system share sheet, and open **offline emergency steps** bundled in the app. Events are logged on the server for research (counts, SMS success, optional coordinates)—not continuous background tracking.

---

## 3.6 — Health Support Network

The Network tab is a **hub** with: Find a nurse (online directory), Chat with assigned nurse, AI chat & voice, Nearby facilities (pilot list), Danger signs / emergency guide, Warning-sign check-in. Pilot deployment uses **seeded provider presence**; live staffing integration is future work.

---

## Scope note (Cameroon)

State explicitly: **French/English UI**, intermittent connectivity (offline emergency content, local caches), SMS-based alerting where smartphones support it, and simple/large-touch SOS UI for literacy accessibility.
