# Generated by Django 4.1.1 on 2022-11-11 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tarefas", "0006_remove_soda_created_at_soda_inicio_alter_soda_area_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="soda",
            name="comentario",
            field=models.CharField(blank=True, default="", max_length=5048),
        ),
        migrations.AlterField(
            model_name="soda",
            name="descricao",
            field=models.CharField(blank=True, default="", max_length=5048),
        ),
    ]
