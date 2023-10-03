# Generated by Django 4.2.5 on 2023-10-03 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactUs",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=200)),
                ("message", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Services",
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
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("created_data", models.DateTimeField(auto_now_add=True)),
                ("updated_data", models.DateTimeField(auto_now=True)),
                ("status", models.BooleanField(default=False)),
            ],
            options={"ordering": ["-created_data"],},
        ),
        migrations.CreateModel(
            name="Team",
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
                ("fullname", models.CharField(max_length=100)),
                ("job", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("image", models.ImageField(default="user.png", upload_to="team")),
                ("twitter", models.CharField(default="#", max_length=255)),
                ("facebook", models.CharField(default="#", max_length=255)),
                ("instagram", models.CharField(default="#", max_length=255)),
                ("linkdin", models.CharField(default="#", max_length=255)),
                ("status", models.BooleanField(default=False)),
                ("updated_datetime", models.DateTimeField(auto_now=True)),
                (
                    "info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
