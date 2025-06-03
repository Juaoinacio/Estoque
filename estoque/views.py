from django.contrib import messages
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
            messages.error(request, "Metodo não permitido")
            return redirect(reverse("index_produto"))
    except Exception as e:
        messages.error(request, str(e))
        print(e)
        return redirect(reverse('index_produto'))
    
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
            return render('index_estoque')
    except Exception as e:
        messages.error(request, str(e))
        print(e)
        return redirect(reverse("show_estoque", kwargs={"id": request.GET["id"]}))
    
def add(request):
    try:
        if request.method == "GET":
            context = {

            }
            return render(request, "estoque_forms_entrada.html", context)
          
    except Exception as e:
        messages.error(request, str(e))
        print(e)
        return redirect(reverse('index_estoque_entrada'))
        





