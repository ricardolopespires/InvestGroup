# Generated by Django 5.1.6 on 2025-05-12 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0006_alter_asset_asset_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='investmentagent',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='agents/images/'),
        ),
    ]
