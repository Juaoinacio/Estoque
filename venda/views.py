from django.shortcuts import render
from .models import ItemVenda, Venda, TipoDePagamento, Produto
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    try:
        if request.method == "GET":
            vendas = Venda.objects.all()

            arrayEntradaGeral = []
            for v in vendas:
                if vendas.exists():
                    dados = {
                        "notaFiscal": v.notaFiscal,
                        "tipoDePagamento": v.tipoDePagamento,
                        "valorTotal": v.valor_total,
                        "data": v.date
                    }
                arrayEntradaGeral.append(dados)

            context = {
                "vendas": arrayEntradaGeral
            }

            return render(request, "vender.html", context)
    except:
        pass
