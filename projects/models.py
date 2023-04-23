from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    ended = models.BooleanField(default=False)
    responsible_user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="responsible_user"
    )
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk": self.pk})


class ProjectRole(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="roles")
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="project_roles",
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user}: {self.name} at {self.project.name}"


class ProjectRoleReview(models.Model):
    role = models.ForeignKey(
        ProjectRole,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    reviewer_role = models.ForeignKey(
        ProjectRole,
        on_delete=models.CASCADE,
        related_name="reviews_written",
    )
    text = models.TextField()
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )

    def __str__(self):
        return f"{self.reviewer_role.user.email} - {self.role.user.email}"
