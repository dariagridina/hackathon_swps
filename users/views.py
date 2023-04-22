from django.contrib.auth.views import LoginView as DjangoLoginView
from django.views.generic import DetailView, ListView

from users.models import User
from users.forms import LoginForm


class LoginView(DjangoLoginView):
    form_class = LoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        remember = form.cleaned_data["remember"]
        if not remember:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super().form_valid(form)


class UserProfileDetailView(DetailView):
    model = User


class UserProfileListView(ListView):
    model = User

    def get_queryset(self):
        return User.objects.filter(profile__isnull=False)
