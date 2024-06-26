# Generated by Django 3.2.25 on 2024-04-16 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_rename_label_answer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answers',
        ),
        migrations.AddField(
            model_name='question',
            name='answers',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='questions_answer', to='quiz.answer'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='questions',
        ),
        migrations.AddField(
            model_name='quiz',
            name='questions',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='question_list', to='quiz.question'),
            preserve_default=False,
        ),
    ]
