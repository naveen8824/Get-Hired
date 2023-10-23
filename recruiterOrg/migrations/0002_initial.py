# Generated by Django 4.2.6 on 2023-10-22 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recruiterOrg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='recruiter',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
