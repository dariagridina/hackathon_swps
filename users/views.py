from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, FormView

from users.forms import LoginForm, RegistrationForm, UserProfileEditForm
from users.models import User, UserSkill, UserProfile


class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = "users/registration.html"
    success_url = reverse_lazy("edit_profile")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        UserProfile.objects.create(user=user)
        login(self.request, user)
        return super().form_valid(form)


class LoginView(DjangoLoginView):
    form_class = LoginForm
    template_name = "users/login.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        remember = form.cleaned_data["remember"]
        if not remember:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super().form_valid(form)


class UserProfileDetailView(DetailView):
    model = User


class UserProfileEditView(FormView):
    form_class = UserProfileEditForm
    template_name = "users/edit_profile.html"

    def get_success_url(self):
        return reverse_lazy("user_detail", kwargs={"pk": self.request.user.pk})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserProfileListView(ListView):
    model = User

    def get_queryset(self):
        qs = User.objects.filter(profile__isnull=False)
        skill = self.request.GET.get("skill")
        if skill:
            print("skill: ", skill)
            qs = qs.filter(skill__name=skill)
        city = self.request.GET.get("city")
        if city:
            print("city: ", city)
            qs = qs.filter(profile__location=city)
        name = self.request.GET.get("name")
        if name:
            print("name: ", name)
            qs = qs.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        return qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = self.get_queryset()
        if qs.exists():
            context["skills"] = list(
                UserSkill.objects.filter(user__in=qs)
                .values_list("name", flat=True)
                .order_by("name")
                .distinct()
            )
            context["cities"] = list(
                User.objects.filter(id__in=qs)
                .exclude(is_staff=True)
                .values_list("profile__location", flat=True)
                .order_by("profile__location")
                .distinct()
            )
        return context
