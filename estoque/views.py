from django.shortcuts import render, redirect, get_object_or_404
from .models import Estoque
def entrada(request):
    try:
        if request.method == "GET":
            entradas = Estoque.objects.filter(movimento='E')
            content = {
                "entradas": entradas
            }
            return render(request, "estoque_entrada.html", content)
    except:
        return redirect("produto")
    
def detalhe_entrada(request, id):
    try:
        if request.method == "GET":
            entrada = Estoque.objects.get(id=id)
            content = {
                "entrada": entrada
            }
            return render(request, "estoque_detalhe_entrada.html", content)
    except:
        return redirect("produto")





