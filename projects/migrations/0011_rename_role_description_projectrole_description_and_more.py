# Generated by Django 4.2 on 2023-04-22 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0010_alter_projectrole_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="projectrole",
            old_name="role_description",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="projectrole",
            old_name="role",
            new_name="name",
        ),
    ]
