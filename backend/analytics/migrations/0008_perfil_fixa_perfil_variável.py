# Generated by Django 5.1.6 on 2025-04-15 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0007_rename_risktolerance_perfil_risk_tolerance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='fixa',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='perfil',
            name='variável',
            field=models.IntegerField(default=0),
        ),
    ]
