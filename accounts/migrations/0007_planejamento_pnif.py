# Generated by Django 4.1.3 on 2023-05-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_planejamento_emergencia_alter_planejamento_pi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='planejamento',
            name='pnif',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Patrimônio Necessário para a Independência Financeira', max_digits=5),
        ),
    ]