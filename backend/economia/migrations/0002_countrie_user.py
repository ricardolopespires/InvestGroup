# Generated by Django 3.2.25 on 2024-04-26 23:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('economia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='countrie',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='user_favoritos', to=settings.AUTH_USER_MODEL),
        ),
    ]
