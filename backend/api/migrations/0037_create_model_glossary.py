# Generated by Django 3.0.4 on 2020-06-22 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0036_improve_model_stats"),
    ]

    operations = [
        migrations.CreateModel(
            name="Glossary",
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
                ("name", models.CharField(help_text="Le mot ou sigle", max_length=50)),
                (
                    "name_alternatives",
                    models.TextField(blank=True, help_text="Des noms alternatifs"),
                ),
                (
                    "definition_short",
                    models.CharField(
                        help_text="La definition succinte du mot", max_length=150
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="Une description longue du mot"
                    ),
                ),
                (
                    "description_accessible_url",
                    models.URLField(
                        blank=True,
                        help_text="Un lien pour aller plus loin",
                        max_length=500,
                    ),
                ),
                (
                    "added",
                    models.DateField(
                        blank=True, help_text="La date d'ajout du mot", null=True
                    ),
                ),
                (
                    "created",
                    models.DateField(
                        auto_now_add=True, help_text="La date de création du mot"
                    ),
                ),
                ("updated", models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name="glossary",
            constraint=models.UniqueConstraint(
                fields=("name",), name="unique glossary name"
            ),
        ),
    ]
