# Generated by Django 4.2.6 on 2023-10-23 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicantDetails', '0005_applicantdetails_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantdetails',
            name='cv',
            field=models.FileField(blank=True, max_length=250, null=True, upload_to='cv/'),
        ),
    ]
