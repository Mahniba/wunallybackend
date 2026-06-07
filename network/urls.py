from django.urls import path

from .views import AssignProviderView, FacilityListView, MyAssignmentView, ProviderListView

urlpatterns = [
    path("providers/", ProviderListView.as_view(), name="network-providers"),
    path("facilities/", FacilityListView.as_view(), name="network-facilities"),
    path("assign/", AssignProviderView.as_view(), name="network-assign"),
    path("assignment/", MyAssignmentView.as_view(), name="network-my-assignment"),
]
