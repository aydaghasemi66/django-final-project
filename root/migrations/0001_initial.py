# Generated by Django 4.2.5 on 2023-09-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
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
    ]
