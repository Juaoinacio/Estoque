from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Estoque

def index(request):
    try:
        if request.method == "GET":
            entradas = Estoque.objects.filter(movimento='E')
            content = {
                "entradas": entradas
            }
            return render(request, "estoque_entrada.html", content)
        else:
            messages.error(request, str(e))
            print(e)
            return HttpResponseRedirect(reverse('index_estoque'))
    except Exception as e:
        messages.error(request, str(e))
        print(e)
        return HttpResponseRedirect(reverse('index_estoque'))
    
def show(request, id):
    try:
        if request.method == "GET":
            entrada = Estoque.objects.get(id=id)
            content = {
                "entrada": entrada
            }
            return render(request, "estoque_detalhe_entrada.html", content)
        else:
            messages.error(request, str(e))
            print(e)
            return HttpResponseRedirect(reverse('index_estoque'))
    except Exception as e:
        messages.error(request, str(e))
        print(e)
        return HttpResponseRedirect(reverse('index_estoque'))
        





