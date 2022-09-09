# Generated by Django 4.1 on 2022-09-08 07:47

from django.db import migrations, models
import login.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NewUser",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email adress"
                    ),
                ),
                ("user_name", models.CharField(max_length=150, unique=True)),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("is_student", models.BooleanField(default=True)),
                ("university", models.CharField(max_length=150)),
                ("level", models.CharField(max_length=150)),
                ("company", models.CharField(max_length=150)),
                ("is_residence", models.BooleanField(default=False)),
                ("residence", models.CharField(max_length=150)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=False)),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True,
                        max_length=255,
                        upload_to=login.models.get_profile_image_filepath,
                    ),
                ),
                (
                    "student_card",
                    models.ImageField(
                        blank=True,
                        max_length=255,
                        upload_to=login.models.get_student_card_filepath,
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
