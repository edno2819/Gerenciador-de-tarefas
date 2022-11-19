# Generated by Django 4.1.1 on 2022-11-16 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("utils", "0008_anotacao_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="anotacao",
            name="author",
            field=models.ForeignKey(
                default=1,
                editable=False,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]