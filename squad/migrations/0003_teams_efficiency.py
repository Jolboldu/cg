# Generated by Django 2.1.7 on 2019-03-31 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squad', '0002_teams_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='efficiency',
            field=models.FloatField(default=100.0),
        ),
    ]
