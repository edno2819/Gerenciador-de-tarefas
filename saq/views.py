from django.shortcuts import render
from .forms import *
from tarefas.models import Soda
from django.db.models import Count



def FormSaq(request):
    if request.method == "GET":
        form = SaqMesDigitacao()
        return render(request, 'MesDigitacao.html', {"form": form})
    else:
        form = SaqMesDigitacao(request.POST)
        if form.is_valid():
            saq = form.save()
            form = SaqMesDigitacao()
        return render(request, 'MesDigitacao.html', {"form": form, "resultado":True})

            
def coletas(request):
    itens_por_areas = {}
    teste = list(Soda.objects.filter(status='OK').values('area', 'nome'))

    c = 0
    for item in teste:
        c+=1
        if item['area'] not in itens_por_areas:
             itens_por_areas[item['area']] = {'id': f'key{c}', 'value':[]}
        itens_por_areas[item['area']]['value'].append(item['nome'])

    return render(request, 'coletasAutomaticas.html', {"itens_por_areas": itens_por_areas})

