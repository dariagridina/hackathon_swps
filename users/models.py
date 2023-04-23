from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class EmailUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(_("Email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = EmailUserManager()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})

    def avg_rating(self):
        return self.project_roles.aggregate(models.Avg("reviews__rating"))[
            "reviews__rating__avg"
        ]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=30, blank=True)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)

    def __str__(self):
        return self.user.email


class UserSkill(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="skills",
        related_query_name="skill",
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.email} - {self.name}"
