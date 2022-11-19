from django.contrib import admin
from saq.models import *


@admin.register(DigitacaoProblema)
class DigitacaoProblemaAdmin(admin.ModelAdmin):
    class Meta:
        model = DigitacaoProblema