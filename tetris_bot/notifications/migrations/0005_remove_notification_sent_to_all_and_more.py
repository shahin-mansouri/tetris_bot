# Generated by Django 5.1.3 on 2024-12-27 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_notification_sent_to_all'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='sent_to_all',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='user',
        ),
    ]
