# Generated by Django 5.0.6 on 2024-06-25 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_profile_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(default='NULL', max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='NULL', max_length=255),
        ),
    ]
