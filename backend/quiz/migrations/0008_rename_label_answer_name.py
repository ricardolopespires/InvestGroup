# Generated by Django 3.2.25 on 2024-04-16 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_quiz_questions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='label',
            new_name='name',
        ),
    ]
