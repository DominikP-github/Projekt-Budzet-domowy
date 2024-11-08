# Generated by Django 4.2.9 on 2024-11-05 01:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=180)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='tranzakcje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=180)),
                ('plan', models.FloatField()),
                ('realizacja', models.FloatField()),
                ('saldo', models.FloatField()),
                ('zysk', models.BooleanField()),
                ('miesiac', models.IntegerField(default=11)),
                ('rok', models.IntegerField(default=2024)),
                ('kategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tranzakcje', to='app.kategoria')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
