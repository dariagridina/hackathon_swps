from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import RedirectView

from users.views import (
    UserProfileDetailView,
    UserProfileEditView,
    UserProfileListView,
    LoginView,
    RegisterView,
)

urlpatterns = [
    path(
        "",
        UserProfileListView.as_view(),
        name="user_list",
    ),
    path(
        "<int:pk>/",
        UserProfileDetailView.as_view(),
        name="user_detail",
    ),
    path(
        "profile/edit/",
        UserProfileEditView.as_view(),
        name="edit_profile",
    ),
    path(
        "login/",
        LoginView.as_view(),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
    path(
        "register/",
        RegisterView.as_view(),
        name="register",
    ),
    path(
        "register/complete/",
        RedirectView.as_view(pattern_name="home"),
        name="register_complete",
    ),
]
