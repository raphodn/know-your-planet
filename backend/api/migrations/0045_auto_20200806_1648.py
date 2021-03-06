# Generated by Django 3.0.4 on 2020-08-06 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0044_quiz_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contribution",
            name="type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("nouvelle question", "nouvelle question"),
                    ("commentaire application", "commentaire application"),
                    ("commentaire question", "commentaire question"),
                    ("commentaire quiz", "commentaire quiz"),
                    ("nom application", "nom application"),
                ],
                help_text="Le type de contribution",
                max_length=150,
            ),
        ),
    ]
