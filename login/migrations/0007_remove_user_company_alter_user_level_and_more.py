# Generated by Django 4.1 on 2022-09-08 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0006_user_company_alter_user_level_alter_user_residence_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="company",),
        migrations.AlterField(
            model_name="user", name="level", field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="user", name="residence", field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="user",
            name="university",
            field=models.CharField(max_length=150),
        ),
    ]
