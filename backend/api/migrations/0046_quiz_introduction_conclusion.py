# Generated by Django 3.0.4 on 2020-08-06 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0045_auto_20200806_1648"),
    ]

    operations = [
        migrations.RenameField(
            model_name="quiz", old_name="description", new_name="introduction",
        ),
        migrations.AddField(
            model_name="quiz",
            name="conclusion",
            field=models.TextField(
                blank=True,
                help_text="Une conclusion du quiz et des pistes pour aller plus loin",
            ),
        ),
    ]