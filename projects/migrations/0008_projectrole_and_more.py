# Generated by Django 4.2 on 2023-04-22 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0007_projectmember_role_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectRole",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("role", models.CharField(max_length=100)),
                ("role_description", models.TextField(blank=True, null=True)),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projects.project",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project_roles",
                        to=settings.AUTH_USER_MODEL,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.RenameModel(
            old_name="ProjectMemberReview",
            new_name="ProjectRoleReview",
        ),
        migrations.DeleteModel(
            name="ProjectMember",
        ),
        migrations.AlterField(
            model_name="projectrolereview",
            name="member",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                related_query_name="reviews",
                to="projects.projectrole",
            ),
        ),
    ]
