# Generated by Django 4.1 on 2022-09-08 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0003_universities"),
    ]

    operations = [
        migrations.DeleteModel(name="Universities",),
    ]