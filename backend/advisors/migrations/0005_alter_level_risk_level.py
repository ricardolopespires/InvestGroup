# Generated by Django 5.1.6 on 2025-04-15 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisors', '0004_level_advisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='risk_level',
            field=models.IntegerField(choices=[(1, 'Conservador'), (2, 'Moderado'), (3, 'Agressivo'), (4, 'Ultra Agressivo')], unique=True),
        ),
    ]
