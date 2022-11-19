# Generated by Django 4.1.1 on 2022-11-14 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("utils", "0003_anotacao"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="anotacao",
            options={"verbose_name_plural": "Anotações"},
        ),
        migrations.AddField(
            model_name="anotacao",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
