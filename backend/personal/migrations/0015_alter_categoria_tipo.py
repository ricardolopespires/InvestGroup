# Generated by Django 3.2.25 on 2024-04-22 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0014_alter_categoria_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='tipo',
            field=models.CharField(choices=[('Renda', 'Renda'), ('Habitação', 'Habitação'), ('Transporte', 'Transporte'), ('Alimentação', 'Alimentação'), ('Saúde', 'Saúde'), ('Educação', 'Educação'), ('Impostos', 'Impostos'), ('Cuidados pessoais', 'Cuidados pessoais'), ('Manutenção/ prevenção', 'Manutenção/ prevenção'), ('Transporte', 'Transporte'), ('Vestuario', 'Vestuario'), ('Lazer', 'Lazer'), ('Outros', 'Outros')], default='receitas', max_length=150),
        ),
    ]
