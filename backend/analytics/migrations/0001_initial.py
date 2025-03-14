# Generated by Django 5.1.6 on 2025-02-27 17:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Investidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('renda_mensal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('despesas_mensais', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dividas', models.DecimalField(decimal_places=2, max_digits=10)),
                ('investimentos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('reserva_emergencia', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tolerancia_risco', models.IntegerField(choices=[(1, 'Baixa'), (2, 'Média'), (3, 'Alta')], default=1)),
                ('horizonte_tempo', models.IntegerField(choices=[(1, 'Curto prazo'), (2, 'Médio prazo'), (3, 'Longo prazo')], default=1)),
                ('objetivo', models.CharField(choices=[('seguranca', 'Segurança'), ('crescimento', 'Crescimento'), ('especulacao', 'Especulação')], default='seguranca', max_length=50)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investidores', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
