from django.shortcuts import render, redirect
from django.contrib import messages
from produto.models import Produto, Categoria
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    try:
        if request.method == "GET":
            produtos = Produto.objects.all()
            categorias = Categoria.objects.all()
            messages.error(request, ("Método Http não permitido!"))
            return render(request, "home.html", {'produtos': produtos, 'categorias': categorias})
        elif request.method == "POST":

            cod_barras =  (request.POST.get("cod_barras", 0))
            nome =  (request.POST.get("nome", 0))
            quantidade =  (request.POST.get("quantidade", 0))
            preco =  (request.POST.get("preco", 0))
            id =  (request.POST.get("categoria", 0))
            
            produto = Produto(
                cod_barras = cod_barras,
                nome = nome,
                quantidade = quantidade,
                preco = preco,
                categoria = Categoria.objects.get(id=id)
            )
            
            print('oiii')

            produto.save()
            return HttpResponseRedirect(reverse('home'))
    except Exception as e:
        messages.error(request, str(e))
        print(e)
        return HttpResponseRedirect(reverse('home'))
    
def delete(request, id):
    try:
        if request.method == "POST":
            pass
    except Exception as e:
        pass