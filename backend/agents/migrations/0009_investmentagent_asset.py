# Generated by Django 5.1.6 on 2025-05-12 22:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0008_investmentagent_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='investmentagent',
            name='asset',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='investment_agents', to='agents.asset'),
        ),
    ]
