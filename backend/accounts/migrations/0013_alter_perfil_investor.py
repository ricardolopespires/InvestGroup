# Generated by Django 3.2.25 on 2024-04-18 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_perfil_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='investor',
            field=models.CharField(blank=True, choices=[('Conservador', 'Conservador'), ('Moderado', 'Moderado'), ('Dinâmico', 'Dinâmico'), ('Arrojado', 'Arrojado'), ('Agressivo', 'Agressivo')], default='Conservador', max_length=190, null=True),
        ),
    ]