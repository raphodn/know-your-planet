# Generated by Django 3.1.1 on 2020-11-24 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0053_quiz_difficulty_average"),
    ]

    operations = [
        migrations.AddField(
            model_name="quiz", name="updated", field=models.DateField(auto_now=True),
        ),
    ]
