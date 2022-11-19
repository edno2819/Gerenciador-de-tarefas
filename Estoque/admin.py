from django.contrib import admin
from Estoque.models import *
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportActionModelAdmin


@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ["nome", "descricao", "updated_at"]

    class Meta:
        model = Equipamento


@admin.register(Manutenção)
class ManutençãoAdmin(SummernoteModelAdmin, ImportExportActionModelAdmin):
    summernote_fields = "servico_executado"
    search_fields = ["equipamento", "ordem"]
    list_display = ["equipamento", "ordem", "area", "recebimento", "reparo", "status", "showImg"]
