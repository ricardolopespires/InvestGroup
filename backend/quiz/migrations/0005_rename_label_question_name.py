# Generated by Django 3.2.25 on 2024-04-16 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20240416_1324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='label',
            new_name='name',
        ),
    ]