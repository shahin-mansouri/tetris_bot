# Generated by Django 5.1.3 on 2024-12-29 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_coin_coin_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='coin_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coin',
            name='day',
            field=models.IntegerField(default=1),
        ),
    ]
