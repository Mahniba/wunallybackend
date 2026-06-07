from django.core.management.base import BaseCommand

from network.models import HealthFacility, HealthProvider


class Command(BaseCommand):
    help = "Seed pilot health providers and facilities for WunAlly network UI."

    def handle(self, *args, **options):
        providers = [
            {
                "name": "Marie Nguema",
                "role": "midwife",
                "facility": "Douala District Maternity",
                "phone": "+237 6 70 12 34 56",
                "languages": ["fr", "en"],
                "is_online": True,
                "bio": "Antenatal care and danger-sign counselling.",
            },
            {
                "name": "Grace Fon",
                "role": "nurse",
                "facility": "Bonassama Health Centre",
                "phone": "+237 6 91 23 45 67",
                "languages": ["fr"],
                "is_online": True,
                "bio": "Maternal health education and referrals.",
            },
            {
                "name": "Aminata Bello",
                "role": "nurse",
                "facility": "Yaoundé Community Clinic",
                "phone": "+237 6 55 88 99 00",
                "languages": ["fr", "en"],
                "is_online": False,
                "bio": "Emotional support and self-care guidance.",
            },
            {
                "name": "Clarisse Mbarga",
                "role": "midwife",
                "facility": "Bafoussam Women's Health Unit",
                "phone": "+237 6 77 44 33 22",
                "languages": ["fr"],
                "is_online": True,
                "bio": "Prenatal visits and warning-sign awareness.",
            },
        ]
        for p in providers:
            HealthProvider.objects.update_or_create(
                name=p["name"],
                facility=p["facility"],
                defaults=p,
            )

        facilities = [
            {
                "name": "Laquintinie Hospital",
                "city": "Douala",
                "region": "Littoral",
                "phone": "+237 2 33 40 23 40",
                "services": "Emergency obstetric care, ANC",
            },
            {
                "name": "Bonassama District Hospital",
                "city": "Douala",
                "region": "Littoral",
                "phone": "+237 2 33 50 12 80",
                "services": "ANC, delivery, emergency",
            },
            {
                "name": "Central Hospital Yaoundé",
                "city": "Yaoundé",
                "region": "Centre",
                "phone": "+237 2 22 23 40 36",
                "services": "Maternity, referral centre",
            },
        ]
        for f in facilities:
            HealthFacility.objects.update_or_create(name=f["name"], defaults=f)

        self.stdout.write(self.style.SUCCESS("Network seed data ready."))
