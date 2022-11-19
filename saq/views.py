from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
# Create your views here.



def FormSaq(request):
    if request.method == "GET":
        form = SaqMesDigitacao()
        return render(request, 'MesDigitacao.html', {"form": form})
    else:
        form = SaqMesDigitacao(request.POST)
        if form.is_valid():
            saq = form.save()
            nome = form.data['nome']
            form = SaqMesDigitacao()
        return render(request, 'MesDigitacao.html', {"form": form})

            

def prossFormSaq(request):
    form = SaqMesDigitacao(request.POST)
    if form.is_valid():
        saq = form.save()
        nome = form.data['nome']
        return  HttpResponse(form)