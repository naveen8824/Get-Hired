# Generated by Django 4.2.6 on 2023-10-23 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicantDetails', '0006_alter_applicantdetails_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantdetails',
            name='cv',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='cv/'),
        ),
    ]
