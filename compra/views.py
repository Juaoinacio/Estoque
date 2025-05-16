from django.shortcuts import render
from .models import ItemCompra, Compra, TipoDePagamento, Fornecedor, Produto
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    try:
        if  request.method == "GET":
            context = {'compras': Compra.objects.all(), 'items': ItemCompra.objects.all()}

            return render(request, "comprar.html", context)
        elif request.mothod == "POST":
            
            notaFiscal = request.POST.get("notaFiscal", 0)
            id_fornecedor = request.POST.get("fornecedor", 0)
            id_tipoDePagamento = request.POST.get("tipoDePagamento", 0)

            compra = Compra(
                notaFiscal = notaFiscal,
                fornecedor = Fornecedor.objects.get(id=id_fornecedor),
                tipoDePagamento = TipoDePagamento.objects.get(id=id_tipoDePagamento),
            )

            compra.save()

            id_produto = request.POST.get("id_produto", 0)
            quantidade = request.POST.get("quantidade", 0)
            precoUnitario = request.POST.get("precoUnitario", 0)

            itemCompra = ItemCompra(
                id_produto = Produto.objects.get(id=id_produto),
                compra = compra,
                quantidade = quantidade,
                precoUnitario = precoUnitario,
            )

            itemCompra.save()
            
    except:
        return HttpResponseRedirect(reverse('comprar'))
        

def itemCompra(request):
    try:
        if  request.method == "GET":
            context = {'compras': Compra.objects.all(), 'items': ItemCompra.objects.all()}

            return render(request, "comprar.html", context)
        elif request.method == "POST":



            itemCompra.save()
    except:
        pass

