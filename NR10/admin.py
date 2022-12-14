from django.contrib import admin
from NR10.models import *


@admin.register(Nr10)
class Nr10Admin(admin.ModelAdmin):
    class Meta:
        model = Nr10


@admin.register(Nr10Complementar)
class Nr10ComplementarAdmin(admin.ModelAdmin):
    class Meta:
        model = Nr10Complementar


@admin.register(Asu)
class AsuAdmin(admin.ModelAdmin):
    class Meta:
        model = Asu


@admin.register(Autorizacao)
class AutorizacaoAdmin(admin.ModelAdmin):
    class Meta:
        model = Autorizacao


@admin.register(Luva)
class LuvaAdmin(admin.ModelAdmin):
    class Meta:
        model = Luva


class Nr10ComplementarAdminInline(admin.TabularInline):
    model = Nr10Complementar
    verbose_name = "NR10 Complementar"
    verbose_name_plural = "NR10's Complementares"
    extra = 0


class Nr10AdminInline(admin.TabularInline):
    model = Nr10
    verbose_name = "NR10"
    verbose_name_plural = "NR10's"
    extra = 0


class AsuAdminInline(admin.TabularInline):
    model = Asu
    verbose_name = "Asu"
    verbose_name_plural = "Asu's"
    extra = 0


class AutorizacaoAdminInline(admin.StackedInline):
    model = Autorizacao
    verbose_name = "Autorização"
    verbose_name_plural = "Autorizações"
    extra = 0


class LuvaAdminInline(admin.StackedInline):
    model = Luva
    extra = 0


@admin.register(Eletricista)
class EletricistaAdmin(admin.ModelAdmin):
    search_fields = ["nome", "id_ambev"]
    list_display = [
        "nome",
        "autorizacao",
        "expire_asu",
        "expire_Nr10",
        "expire_Nr10Complementar",
        "expire_Autorizacao",
        "expire_Luva",
    ]
    inlines = [
        Nr10AdminInline,
        Nr10ComplementarAdminInline,
        AsuAdminInline,
        AutorizacaoAdminInline,
        LuvaAdminInline,
    ]

    class Media:
        ...

    # css = {
    #     'all': ('css/admin/my_own_admin.css',)
    # }
