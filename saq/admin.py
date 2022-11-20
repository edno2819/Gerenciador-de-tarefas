from django.contrib import admin
from saq.models import *


@admin.register(DigitacaoProblema)
class DigitacaoProblemaAdmin(admin.ModelAdmin):
    list_display = ["item", "area", "nome"]
    search_fields = ["item", "area", "nome"]

    class Meta:
        model = DigitacaoProblema