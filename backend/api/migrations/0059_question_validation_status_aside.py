# Generated by Django 3.1.1 on 2020-12-01 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0058_ckeditor_textfield_to_richtextfield"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="validation_status",
            field=models.CharField(
                choices=[
                    ("Brouillon", "Brouillon"),
                    ("A valider", "A valider"),
                    ("Validée", "Validée"),
                    ("Écartée temporairement", "Écartée temporairement"),
                    ("Écartée", "Écartée"),
                ],
                default="Brouillon",
                help_text="Le statut de la question dans le workflow de validation",
                max_length=150,
            ),
        ),
    ]
