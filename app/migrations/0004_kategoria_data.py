# Generated by Django 4.2.9 on 2024-11-06 16:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_kategoria_zysk'),
    ]

    operations = [
        migrations.AddField(
            model_name='kategoria',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
