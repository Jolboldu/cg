# Generated by Django 2.1.7 on 2019-03-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignments',
            name='max_grade',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='attendance',
            name='attend',
            field=models.BooleanField(default=False),
        ),
    ]
