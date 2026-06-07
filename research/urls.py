from django.urls import path

from .views import (
    DeleteAccountView,
    EvaluationSubmitView,
    ExportDataView,
    StudyConsentView,
)

urlpatterns = [
    path("export/", ExportDataView.as_view(), name="me-export"),
    path("account/", DeleteAccountView.as_view(), name="me-account-delete"),
    path("consent/", StudyConsentView.as_view(), name="me-consent"),
    path("evaluation/", EvaluationSubmitView.as_view(), name="me-evaluation"),
]
