# Generated by Django 4.2.6 on 2023-10-22 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='orgUpdatedbyRecruiter',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='resumeUpdatedbyApplicant',
            field=models.BooleanField(default=False),
        ),
    ]
