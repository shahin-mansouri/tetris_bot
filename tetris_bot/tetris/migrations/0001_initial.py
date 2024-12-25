# Generated by Django 5.1.3 on 2024-12-25 09:27

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TetrisPlay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('play_date', models.DateField(default=django.utils.timezone.now)),
                ('duration', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tetris_sessions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'play_date')},
            },
        ),
    ]
