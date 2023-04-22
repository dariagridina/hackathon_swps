# Generated by Django 4.2 on 2023-04-22 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0004_projectmemberreview_headline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projectmemberreview",
            name="member",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                related_query_name="reviews",
                to="projects.projectmember",
            ),
        ),
    ]
