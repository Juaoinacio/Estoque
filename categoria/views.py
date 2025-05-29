from django.shortcuts import render
from .models import Categoria

def index(request):
    categorias = Categoria.objects.all()

    return render(request, "index.html", {"categorias":categorias})