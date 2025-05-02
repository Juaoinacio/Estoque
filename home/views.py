from django.shortcuts import render
from django.contrib import messages
from categoria.models import Categoria

def index(request):
    try:
        if request.method == "GET":
            categorias = Categoria.objects.all()
            return render(request, "home.html", {'categorias': categorias})
        messages.error(request, ("Método Http não permitido!"))
    except Exception as e:
        messages.error(request, str(e))