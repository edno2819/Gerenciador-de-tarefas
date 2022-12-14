# Generated by Django 4.1.1 on 2022-11-14 15:03

from django.db import migrations, models
import django.utils.timezone
import utils.models


class Migration(migrations.Migration):

    dependencies = [
        ("utils", "0002_area"),
    ]

    operations = [
        migrations.CreateModel(
            name="Anotacao",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=40)),
                ("anotacao", models.CharField(default=" ", max_length=10048)),
                (
                    "updated_at",
                    utils.models.AutoDateTimeField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Anotações Individuais",
            },
        ),
    ]
