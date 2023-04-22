from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from users.views import UserProfileDetailView, UserProfileListView, LoginView

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
        "settings/",
        TemplateView.as_view(
            template_name="users/user_settings.html"
        ),  # TODO: Create this view
        name="settings",
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
]
