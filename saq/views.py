from django.shortcuts import render
from .forms import *



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

            
