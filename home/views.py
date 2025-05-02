from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages

def index(request):
    try:
        if request.method == "GET":
            return render(request, "home.html")
        messages.error(request, _("Método Http não permitido!"))
    except Exception as e:
        messages.error(request, str(e))