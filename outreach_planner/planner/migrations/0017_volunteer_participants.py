# Generated by Django 4.1.2 on 2022-11-01 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0016_submisson_delete_inbox'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='participants',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
