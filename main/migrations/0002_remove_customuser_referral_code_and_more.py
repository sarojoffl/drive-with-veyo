# Generated by Django 5.2.1 on 2025-05-11 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='referral_code',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='zip_code',
        ),
    ]
