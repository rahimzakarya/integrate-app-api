# Generated by Django 4.1 on 2022-09-08 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0011_rename_name_resources_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="resources", old_name="user", new_name="user_publish",
        ),
    ]
