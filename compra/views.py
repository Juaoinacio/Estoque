from django.shortcuts import render
from .models import ItemCompra, Compra
def index(request):
    try:
        if  request.method == "GET":
            context = {'compra': Compra.objects.all(), 'item': ItemCompra.objects.all()}

            return render(request, "comprar.html", context)
        else:
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
