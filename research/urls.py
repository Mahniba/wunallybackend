from django.urls import path

from .views import DeleteAccountView, ExportDataView

urlpatterns = [
    path("export/", ExportDataView.as_view(), name="me-export"),
    path("account/", DeleteAccountView.as_view(), name="me-account-delete"),
]
