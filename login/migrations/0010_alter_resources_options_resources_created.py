# Generated by Django 4.1 on 2022-09-08 09:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0009_rename_user_newuser_resources"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="resources", options={"ordering": ["-created"]},
        ),
        migrations.AddField(
            model_name="resources",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
