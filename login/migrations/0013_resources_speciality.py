# Generated by Django 4.1 on 2022-09-08 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0012_rename_user_resources_user_publish"),
    ]

    operations = [
        migrations.AddField(
            model_name="resources",
            name="speciality",
            field=models.CharField(max_length=150, null=True),
        ),
    ]
