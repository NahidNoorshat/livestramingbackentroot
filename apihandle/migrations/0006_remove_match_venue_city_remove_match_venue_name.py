# Generated by Django 5.0 on 2024-06-27 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("apihandle", "0005_match_liveurl"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="match",
            name="venue_city",
        ),
        migrations.RemoveField(
            model_name="match",
            name="venue_name",
        ),
    ]
