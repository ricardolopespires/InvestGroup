# Generated by Django 4.1.3 on 2023-05-26 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoal', '0017_reserva_emergencia_view_planejamento'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reserva_Emergencia_View',
            new_name='Reserva',
        ),
    ]