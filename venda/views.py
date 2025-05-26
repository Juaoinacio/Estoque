from django.shortcuts import render
from .models import ItemVenda, Venda, TipoDePagamento, Produto
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    try:
        if request.method == "GET":
            vendas = Venda.objects.all()

            arrayEntradaGeral = []
            context = {
                "vendas": arrayEntradaGeral
            }

            return render(request, "vender.html", arrayEntradaGeral)
    except:
        pass
