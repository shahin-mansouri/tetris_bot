# Generated by Django 5.1.3 on 2024-12-13 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramuser',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$870000$TnXjrrerfxarm3iIvwqulc$fbFrlSpZ8FL3fY5vHttQscMMA0SVAqbJ2M2zFliig8I=', max_length=128),
        ),
    ]
