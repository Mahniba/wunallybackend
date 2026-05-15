from django.urls import path

from .views import MoodListCreateView, PersonalizedTipsView, SymptomListCreateView

urlpatterns = [
    path("symptoms/", SymptomListCreateView.as_view(), name="me-symptoms"),
    path("moods/", MoodListCreateView.as_view(), name="me-moods"),
    path("tips/", PersonalizedTipsView.as_view(), name="me-tips"),
]
