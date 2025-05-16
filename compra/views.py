from django.shortcuts import render

def index(request):
    try:
        if  request.method == "GET":
               

            return render(request, "comprar.html")
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
