# Generated by Django 4.1.3 on 2022-11-20 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("NR10", "0004_alter_luva_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="luva",
            name="status",
        ),
    ]
