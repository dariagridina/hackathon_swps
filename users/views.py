from django.views.generic import DetailView

from users.models import User


class UserProfileDetailView(DetailView):
    model = User
    template_name = "users/user_profile_detail.html"
    context_object_name = "user"
