# Generated by Django 3.2.25 on 2024-04-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_remove_question_answers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='order',
        ),
        migrations.AlterField(
            model_name='answer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]