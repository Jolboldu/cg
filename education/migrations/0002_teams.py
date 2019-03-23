# Generated by Django 2.1.7 on 2019-03-23 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0001_initial'),
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.Courses')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_user.Student')),
            ],
        ),
    ]
