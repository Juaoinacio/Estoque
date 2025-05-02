from django.shortcuts import render
from django.contrib import messages
from produto.models import Produto

def index(request):
    try:
        if request.method == "GET":
            produtos = Produto.objects.all()
            return render(request, "home.html", {'produtos': produtos})
        messages.error(request, ("Método Http não permitido!"))
    except Exception as e:
        messages.error(request, str(e))