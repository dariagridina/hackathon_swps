# Generated by Django 4.2 on 2023-04-22 08:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0008_projectrole_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="projectrole",
            unique_together={("project", "user")},
        ),
    ]
