# Generated by Django 4.2.9 on 2024-11-06 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_tranzakcje_miesiac_remove_tranzakcje_rok_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategoria',
            name='zysk',
            field=models.BooleanField(),
        ),
    ]
