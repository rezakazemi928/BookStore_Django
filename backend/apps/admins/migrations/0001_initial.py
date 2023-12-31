# Generated by Django 4.0 on 2023-09-05 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AdminModel",
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
                ("firstname", models.CharField(max_length=100)),
                ("lastname", models.CharField(max_length=100)),
                ("username", models.CharField(max_length=100, unique=True)),
                (
                    "email",
                    models.EmailField(blank=True, max_length=255, null=True, unique=True),
                ),
            ],
        ),
    ]
