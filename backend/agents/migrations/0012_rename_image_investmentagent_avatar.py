# Generated by Django 5.1.6 on 2025-05-12 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0011_alter_investmentagent_asset'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investmentagent',
            old_name='image',
            new_name='avatar',
        ),
    ]
