# Generated by Django 4.1 on 2022-09-08 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0004_delete_universities"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="company",),
    ]
