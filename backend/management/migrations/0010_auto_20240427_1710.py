# Generated by Django 3.2.25 on 2024-04-27 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_auto_20240427_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='strategic',
        ),
        migrations.AddField(
            model_name='situacao',
            name='strategic',
            field=models.ManyToManyField(blank=True, help_text='Estrategias', related_name='estrategicas', to='management.Strategy'),
        ),
    ]
