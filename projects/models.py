from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    ended = models.BooleanField(default=False)
    responsible_user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="responsible_user"
    )


class ProjectTag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)


class ProjectMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, unique=True)
