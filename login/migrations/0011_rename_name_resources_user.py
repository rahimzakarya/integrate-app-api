# Generated by Django 4.1 on 2022-09-08 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0010_alter_resources_options_resources_created"),
    ]

    operations = [
        migrations.RenameField(
            model_name="resources", old_name="name", new_name="user",
        ),
    ]
