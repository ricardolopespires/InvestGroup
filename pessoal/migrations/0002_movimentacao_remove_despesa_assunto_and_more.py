# Generated by Django 4.1.3 on 2023-05-23 11:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pessoal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.CharField(max_length=90, primary_key=True, serialize=False)),
                ('real', models.DecimalField(decimal_places=2, max_digits=5)),
                ('status', models.CharField(choices=[('receitas', 'Receitas'), ('despesas', 'Despesas')], default='receitas', max_length=150)),
                ('previsto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('atual', models.DecimalField(decimal_places=2, max_digits=5)),
                ('diferenca', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('variacao', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorie', to='pessoal.categoria')),
                ('user', models.ManyToManyField(blank=True, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Receita',
                'verbose_name_plural': 'Receitas',
                'ordering': ['-created'],
            },
        ),
        migrations.RemoveField(
            model_name='despesa',
            name='assunto',
        ),
        migrations.RemoveField(
            model_name='despesa',
            name='user',
        ),
        migrations.RemoveField(
            model_name='receita',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='receita',
            name='user',
        ),
        migrations.DeleteModel(
            name='Assunto',
        ),
        migrations.DeleteModel(
            name='Despesa',
        ),
        migrations.DeleteModel(
            name='Receita',
        ),
    ]