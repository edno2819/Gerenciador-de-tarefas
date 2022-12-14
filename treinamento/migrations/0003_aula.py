# Generated by Django 4.1.1 on 2022-11-16 18:33

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import treinamento.models


class Migration(migrations.Migration):

    dependencies = [
        ("treinamento", "0002_rename_aula_referencia"),
    ]

    operations = [
        migrations.CreateModel(
            name="Aula",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=40)),
                ("descricao", models.CharField(blank=True, max_length=1200, null=True)),
                (
                    "video",
                    models.FileField(
                        null=True,
                        upload_to="videos_uploaded",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["MOV", "avi", "mp4", "webm", "mkv"]
                            )
                        ],
                    ),
                ),
                (
                    "create_at",
                    treinamento.models.AutoDateTimeField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
            ],
        ),
    ]
