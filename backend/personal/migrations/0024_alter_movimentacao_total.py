# Generated by Django 3.2.25 on 2024-04-23 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0023_alter_movimentacao_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacao',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, help_text='O valor Total do documento', max_digits=10),
        ),
    ]