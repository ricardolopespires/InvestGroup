# Generated by Django 3.2.25 on 2024-04-27 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_situacao_strategic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='situacao',
            name='portfolio',
        ),
        migrations.RemoveField(
            model_name='situacao',
            name='strategic',
        ),
        migrations.RemoveField(
            model_name='situacao',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='strategy',
            name='situacao',
        ),
        migrations.DeleteModel(
            name='Perfil',
        ),
        migrations.DeleteModel(
            name='Portfolio',
        ),
        migrations.DeleteModel(
            name='Situacao',
        ),
        migrations.DeleteModel(
            name='Strategy',
        ),
    ]