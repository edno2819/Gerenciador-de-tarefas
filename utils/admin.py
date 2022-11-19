from django.contrib import admin
from utils.models import *
from import_export.admin import ImportExportActionModelAdmin
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Link)
class linksAdmin(ImportExportActionModelAdmin):
    search_fields = ["nome"]
    list_filter = ["nome"]
    list_display = ["nome", "link_admin"]


@admin.register(Arquivo)
class arquivosAdmin(admin.ModelAdmin):
    search_fields = ["nome"]
    list_filter = ["nome"]
    list_display = ["nome", "path"]


@admin.register(Area)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ["nome"]

    class Meta:
        model = Area


@admin.register(Anotacao)
class AnotacaoAdmin(SummernoteModelAdmin, ImportExportActionModelAdmin):
    summernote_fields = "anotacao"
    search_fields = ["nome"]
    list_display = ["nome", "updated_at", 'quote']
    ordering = ("-updated_at",)

    def get_queryset(self, request):
        qs = super(AnotacaoAdmin, self).get_queryset(request)
        # if request.user.is_superuser:
        #     return qs
        return qs.filter(author=request.user)

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change:
            instance.author = user
        instance.save()
        form.save_m2m()
        return instance

    class Meta:
        model = Anotacao
