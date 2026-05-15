from django.urls import path

from .views import (
    CarePlanView,
    ContactDetailView,
    ContactListCreateView,
    ReminderDetailView,
    ReminderListCreateView,
)

urlpatterns = [
    path("reminders/", ReminderListCreateView.as_view(), name="me-reminders"),
    path("reminders/<int:pk>/", ReminderDetailView.as_view(), name="me-reminder-detail"),
    path("contacts/", ContactListCreateView.as_view(), name="me-contacts"),
    path("contacts/<int:pk>/", ContactDetailView.as_view(), name="me-contact-detail"),
    path("care-plan/", CarePlanView.as_view(), name="me-care-plan"),
]
