from treinamento.models import *
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin, messages
from django.shortcuts import redirect
from django.urls import path

#link para criar cotões personalizados
#https://www.dicas-de-django.com.br/32-django-admin-sobreescrevendo-os-templates-do-admin#


@admin.register(Referencia)
class referenciaAdmin(SummernoteModelAdmin):
    summernote_fields = ('descricao')
    search_fields = ['nome']
    list_filter = ['nome']
    list_display = ["nome", 'descricao_aula', 'embbed_aula']


@admin.register(Aula)
class aulasAdmin(SummernoteModelAdmin):
    summernote_fields = ('descricao')
    search_fields = ['nome']
    list_filter = ['nome']
    list_display = ["nome", 'descricao_aula']


    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                'botao-artigo/',
                self.admin_site.admin_view(self.minha_funcao, cacheable=True)
            ),
        ]
        return my_urls + urls

    def minha_funcao(self, request):
        print('Ao clicar no botão, faz alguma coisa...')
        messages.add_message(
            request,
            messages.INFO,
            'Ação realizada com sucesso.'
        )
        return redirect('admin:core_article_changelist')
