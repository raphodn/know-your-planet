# Generated by Django 3.1.4 on 2021-01-25 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0073_configuration_notion_questions_scope_5_last_imported"),
    ]

    operations = [
        migrations.AddField(
            model_name="configuration",
            name="application_frontend_ecoindex_url",
            field=models.URLField(
                blank=True,
                help_text="Le lien vers le test EcoIndex.fr du frontend",
                max_length=500,
            ),
        ),
    ]
