# Generated by Django 4.1.3 on 2023-05-25 19:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pessoal', '0013_movimentacao_total_alter_movimentacao_valor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Financeiro',
            fields=[
                ('id', models.CharField(max_length=90, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('receitas', models.DecimalField(decimal_places=2, default=0, help_text='O valor das receitas', max_digits=10)),
                ('despesas', models.DecimalField(decimal_places=2, default=0, help_text='O valor das despesas', max_digits=10)),
                ('cartao', models.DecimalField(decimal_places=2, default=0, help_text='O valor das despesas', max_digits=10)),
                ('investimento', models.DecimalField(decimal_places=2, default=0, help_text='O valor dos cartões', max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, default=0, help_text='O valor dos investimentos', max_digits=10)),
                ('user', models.ManyToManyField(blank=True, related_name='financeiro_pessoal', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Receita',
                'verbose_name_plural': 'Receitas',
                'ordering': ['-created'],
            },
        ),
    ]