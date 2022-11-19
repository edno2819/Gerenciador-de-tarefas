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


class Nr10ComplementarAdminInline(admin.TabularInline):
    model = Nr10Complementar
    verbose_name = 'NR10 Complementar'
    verbose_name_plural = "NR10's Complementares"
    extra = 1

class Nr10AdminInline(admin.TabularInline):
    model = Nr10
    verbose_name = 'NR10'
    verbose_name_plural = "NR10's"
    extra = 1
    
class AsuAdminInline(admin.TabularInline):
    model = Asu
    verbose_name = 'Asu'
    verbose_name_plural = "Asu's"
    extra = 1

@admin.register(Eletricista)
class EletricistaAdmin(admin.ModelAdmin):
    # search_fields = ["equipamento", "ordem"]
    # list_display = ["equipamento", "ordem", "recebimento", "status", "showImg"]
    inlines = [Nr10AdminInline, Nr10ComplementarAdminInline, AsuAdminInline]

    
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(EletricistaAdmin, self).get_form(request, obj, **kwargs)
    #     form.base_fields['person'].label_from_instance = lambda inst: "{} {}".format(inst.id, inst.first_name)
    #     return form

    class Media:
        ...

    # css = {
    #     'all': ('css/admin/my_own_admin.css',)
    # }
