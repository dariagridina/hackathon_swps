from pprint import pprint

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from users.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text="Required. Enter a valid email address.",
    )

    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=255)
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )
    remember = forms.BooleanField(required=False)

    error_messages = {
        "invalid_credentials": _("Unable to login with provided credentials."),
        "inactive": _("User account not active."),
    }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email is not None and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_credentials_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(
                self.error_messages["inactive"],
                code="inactive",
            )

    def get_user(self):
        return self.user_cache

    def get_invalid_credentials_error(self):
        return ValidationError(
            self.error_messages["invalid_credentials"],
            code="invalid_credentials",
        )


class UserProfileEditForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=255,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Last name", max_length=255,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(label="Location", max_length=255,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(label="Bio", widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField(label="Avatar", required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'data': 'initial'}))
    github = forms.URLField(label="Github", required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    linkedin = forms.URLField(label="LinkedIn", required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("instance")
        super().__init__(*args, **kwargs)
        self.fields["first_name"].initial = self.user.first_name
        self.fields["last_name"].initial = self.user.last_name
        self.fields["location"].initial = self.user.profile.location
        self.fields["bio"].initial = self.user.profile.bio
        self.fields["image"].initial = self.user.profile.image
        self.fields["github"].initial = self.user.profile.github_url
        self.fields["linkedin"].initial = self.user.profile.linkedin_url

    def save(self):
        self.user.first_name = self.cleaned_data["first_name"]
        self.user.last_name = self.cleaned_data["last_name"]
        self.user.save()

        self.user.profile.bio = self.cleaned_data["bio"]
        self.user.profile.location = self.cleaned_data["location"]
        self.user.profile.github_url = self.cleaned_data["github"]
        self.user.profile.linkedin_url = self.cleaned_data["linkedin"]
        if self.cleaned_data["image"]:
            self.user.profile.image = self.cleaned_data["image"]
        else:
            self.user.profile.image = None
        self.user.profile.save()
