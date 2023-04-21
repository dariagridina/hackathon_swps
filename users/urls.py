from django.urls import path

from users.views import UserProfileDetailView

urlpatterns = [
    path("<int:pk>/", UserProfileDetailView.as_view(), name="user-profile-detail"),
]
