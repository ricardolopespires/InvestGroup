# Generated by Django 4.1.3 on 2023-05-23 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoal', '0004_alter_categoria_options_categoria_tipo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='tipo',
            field=models.CharField(max_length=90, unique=True),
        ),
    ]