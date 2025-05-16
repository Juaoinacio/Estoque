from django.shortcuts import render
from .models import ItemCompra, Compra, TipoDePagamento, Fornecedor

def index(request):
    try:
        if  request.method == "GET":
            context = {'compra': Compra.objects.all(), 'item': ItemCompra.objects.all()}

            return render(request, "comprar.html", context)
        elif request.mothod == "POST":
            
            notaFiscal = request.POST.get("notaFiscal", 0)
            id_fornecedor = request.POST.get("fornecedor", 0)
            id_tipoDePagamento = request.POST.get("tipoDePagamento", 0)
            valor = request.POST.get("somaTotal", 0)

            compra = Compra(
                notaFiscal = notaFiscal,
                fornecedor = Fornecedor.objects.get(id=id_fornecedor),
                tipoDePagamento = TipoDePagamento.objects.get(id=id_tipoDePagamento),
                valor = valor
            )
        #else:
            pass
    except:
        pass
        

def itemCompra(request):
    try:
        if  request.method == "GET":
               

            return render(request, "comprar.html")
        else:
            pass
    except:
        pass

def editarItemCompra(request):
    try:
        if  request.method == "GET":
               

            return render(request, "comprar.html")
        else:
            pass
    except:
        pass
