from django.urls import path

from .jwt_views import DocumentedTokenRefreshView
from .views import LoginView, LogoutView, PasswordResetView, RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password/reset/", PasswordResetView.as_view(), name="password_reset"),
    path("token/refresh/", DocumentedTokenRefreshView.as_view(), name="token_refresh"),
]
