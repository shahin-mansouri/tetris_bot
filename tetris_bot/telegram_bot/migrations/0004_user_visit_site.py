# Generated by Django 5.1.3 on 2024-12-20 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='visit_site',
            field=models.BooleanField(default=False),
        ),
    ]
