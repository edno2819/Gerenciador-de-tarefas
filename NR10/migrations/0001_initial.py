# Generated by Django 4.1.3 on 2022-11-19 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("utils", "0009_alter_anotacao_author"),
    ]

    operations = [
        migrations.CreateModel(
            name="Eletricista",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(blank=True, max_length=15, null=True)),
                ("cargo", models.CharField(blank=True, max_length=40, null=True)),
                (
                    "imagem",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="NR10/foto/",
                        verbose_name="Foto de Perfil",
                    ),
                ),
                (
                    "area",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="utils.area",
                        verbose_name="Área",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Nr10Complementar",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("data", models.DateField()),
                (
                    "certificado",
                    models.FileField(
                        max_length=254, upload_to="NR10/NR10Complementar/"
                    ),
                ),
                (
                    "dono",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nr10_Complementar",
                        to="NR10.eletricista",
                    ),
                ),
            ],
            options={
                "verbose_name": "NR10 Complementar",
                "verbose_name_plural": "NR10's Complementares",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Nr10",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("data", models.DateField()),
                (
                    "certificado",
                    models.FileField(max_length=254, upload_to="NR10/NR10/"),
                ),
                (
                    "dono",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nr10",
                        to="NR10.eletricista",
                    ),
                ),
            ],
            options={
                "verbose_name": "NR10 Complementar",
                "verbose_name_plural": "NR10 Complementar",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Autorizacao",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("data", models.DateField()),
                (
                    "certificado",
                    models.FileField(max_length=254, upload_to="NR10/Autorizacao/"),
                ),
                (
                    "nivel",
                    models.CharField(
                        choices=[
                            (
                                "Eletrico com painel desligado",
                                "Eletrico com painel desligado",
                            ),
                            (
                                "Eletrico com painel ligado",
                                "Eletrico com painel ligado",
                            ),
                            ("Eletrico com alta tensão", "Eletrico com alta tensão"),
                            ("Completo", "Completo"),
                        ],
                        default="Eletrico com painel desligado",
                        max_length=254,
                    ),
                ),
                (
                    "dono",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Autorização",
                        to="NR10.eletricista",
                    ),
                ),
            ],
            options={
                "verbose_name": "Autorização",
                "verbose_name_plural": "Autorizações",
            },
        ),
        migrations.CreateModel(
            name="Asu",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("data", models.DateField()),
                (
                    "certificado",
                    models.FileField(max_length=254, upload_to="NR10/ASU/"),
                ),
                (
                    "dono",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Asu",
                        to="NR10.eletricista",
                    ),
                ),
            ],
            options={
                "verbose_name": "ASU",
                "verbose_name_plural": "ASU's",
            },
        ),
    ]
