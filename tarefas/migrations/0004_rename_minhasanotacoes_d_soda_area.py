# Generated by Django 4.1.1 on 2022-11-11 13:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tarefas', '0003_alter_minhasanotacoes_anotacao_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MinhasAnotacoes',
            new_name='d',
        ),
        migrations.AddField(
            model_name='soda',
            name='area',
            field=models.CharField(choices=[('-', '-'), ('Brassagem 1', 'Brassagem 1'), ('Brassagem 2', 'Brassagem 2'), ('Filtração 1', 'Filtração 1'), ('Filtração 2', 'Filtração 2'), ('Linha 502', 'Linha 502'), ('Linha 502', 'Linha 502'), ('Linha 503', 'Linha 503'), ('Linha 511', 'Linha 511'), ('Linha 512', 'Linha 512'), ('Maturação', 'Maturação'), ('Qualidade', 'Qualidade'), ('Utilidades', 'Utilidades'), ('Maturação', 'Maturação'), ('Adega de Fermento', 'Adega de Fermento')], default='-', max_length=40),
        ),
    ]
