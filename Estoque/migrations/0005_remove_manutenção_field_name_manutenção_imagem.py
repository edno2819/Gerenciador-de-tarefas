# Generated by Django 4.1.1 on 2022-11-12 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Estoque", "0004_manutenção_field_name_alter_manutenção_area_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="manutenção",
            name="field_name",
        ),
        migrations.AddField(
            model_name="manutenção",
            name="imagem",
            field=models.ImageField(
                default=1, upload_to=None, verbose_name="Foto do equipamento"
            ),
            preserve_default=False,
        ),
    ]
