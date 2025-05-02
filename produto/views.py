from django.shortcuts import render
from .models import Produto

def index(request):
    produtos = Produto.objects.all()

    return render(request, "home.html", {"produtos": produtos})