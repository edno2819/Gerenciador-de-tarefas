# Generated by Django 4.1.3 on 2022-11-20 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("NR10", "0003_alter_luva_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="luva",
            name="status",
            field=models.BinaryField(
                choices=[(True, "Ok"), (False, "Irregular")], editable=True
            ),
        ),
    ]
