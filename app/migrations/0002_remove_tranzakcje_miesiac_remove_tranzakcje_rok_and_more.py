# Generated by Django 4.2.9 on 2024-11-05 03:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tranzakcje',
            name='miesiac',
        ),
        migrations.RemoveField(
            model_name='tranzakcje',
            name='rok',
        ),
        migrations.RemoveField(
            model_name='tranzakcje',
            name='zysk',
        ),
        migrations.AddField(
            model_name='kategoria',
            name='zysk',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tranzakcje',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
