from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    ended = models.BooleanField(default=False)
    responsible_user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="responsible_user"
    )

    def __str__(self):
        return self.name


class ProjectTag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag


class ProjectMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        unique=True,
        related_name="project_memberships",
    )


class ProjectMemberReview(models.Model):
    member = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews_received",
        related_query_name="review_received",
    )
    reviewer = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews_written",
        related_query_name="review_written",
    )
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        related_name="reviews",
        related_query_name="review",
    )
    text = models.TextField()
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )

    def __str__(self):
        return f"{self.reviewer.email} - {self.member.email}"
