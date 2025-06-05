from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Estoque, EstoqueItem
from produto.models import Produto

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
            produto = Produto.objects.all()
            estoque = Estoque.objects.filter().values("id", "nf")

            if produto.exists() and estoque.exists():
                context = {
                    "produto" : produto,
                    "estoque" : estoque,
                }
                print(produto)
            return render(request, "estoque_forms_entrada.html", context)
        elif request.method == "POST":
            
            id_estoque = request.POST.get("id_estoque")
            id_produto = request.POST.get("id_produto")
            quantidade = request.POST.get("quantidade")
            print(id_estoque,id_produto,quantidade)

            entrada = EstoqueItem (
                estoque = Estoque.objects.get(id=id_estoque),
                produto = Produto.objects.get(id=id_produto),
                quantidade = quantidade,


            )

            entrada.save()

    except Exception as e:
        messages.error(request, str(e))
        print(e)
        return redirect(reverse('index_estoque_entrada'))






