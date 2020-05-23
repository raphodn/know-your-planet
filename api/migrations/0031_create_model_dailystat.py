# Generated by Django 3.0.4 on 2020-05-23 08:16

import api.constants
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0030_create_model_questionfeedback"),
    ]

    operations = [
        migrations.CreateModel(
            name="DailyStat",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(help_text="Le jour de la statistique")),
                (
                    "question_answer_count",
                    models.PositiveIntegerField(
                        default=0, help_text="Le nombre de questions répondues"
                    ),
                ),
                (
                    "question_answer_from_quiz_count",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Le nombre de questions répondues au sein de quizs",
                    ),
                ),
                (
                    "quiz_answer_count",
                    models.PositiveIntegerField(
                        default=0, help_text="Le nombre de quizs répondus"
                    ),
                ),
                (
                    "question_feedback_count",
                    models.PositiveIntegerField(
                        default=0, help_text="Le nombre de feedbacks aux questions"
                    ),
                ),
                (
                    "question_feedback_from_quiz_count",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Le nombre de feedbacks aux questions au sein de quizs",
                    ),
                ),
                (
                    "hour_split",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        default=api.constants.daily_stat_hour_split_jsonfield_default_value,
                        help_text="Les statistiques par heure",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="La date & heure de la stat journalière",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="question",
            name="answer_count",
            field=models.PositiveIntegerField(
                default=0, help_text="Le nombre de réponses"
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="answer_success_count",
            field=models.PositiveIntegerField(
                default=0, help_text="Le nombre de réponses correctes"
            ),
        ),
    ]
