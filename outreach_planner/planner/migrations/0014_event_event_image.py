# Generated by Django 4.1.2 on 2022-10-31 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("planner", "0013_venue_venue_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="event_image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
