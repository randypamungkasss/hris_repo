# Generated by Django 5.2 on 2025-04-13 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("workspaces", "0002_departement_is_active"),
    ]

    operations = [
        migrations.RenameField(
            model_name="departementmember",
            old_name="departemnet",
            new_name="departement",
        ),
    ]
