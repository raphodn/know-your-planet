# Generated by Django 3.1.4 on 2021-01-12 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0070_quiz_questions_through_update_data"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="quizquestion", unique_together={("quiz", "question")},
        ),
    ]
