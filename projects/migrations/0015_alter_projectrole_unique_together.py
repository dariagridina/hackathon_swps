# Generated by Django 4.2 on 2023-04-22 11:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0014_rename_reviewer_projectrolereview_reviewer_role"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="projectrole",
            unique_together=set(),
        ),
    ]
