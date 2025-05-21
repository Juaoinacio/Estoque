from django.shortcuts import render
from .models import ItemVenda, Venda, TipoDePagamento, Produto
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    try:
        if request.method == "GET":
            context = {
                "vendas": Venda.objects.all(),
                "itens": ItemVenda.objects.all(),
                "tiposdepagamentos": TipoDePagamento.objects.all(),
            }

            return render(request, "vender.html", context)
    except:
        pass
