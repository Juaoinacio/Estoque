from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from produto.models import Produto, Categoria
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


def index(request):
    minimo = Produto.objects.filter(quantidade__gte=100, quantidade__lte=200)

    valorMinimo = len(minimo)
    critico = Produto.objects.filter(quantidade__gte=1, quantidade__lte=100)

    valorCritico = len(critico)
    zerado = Produto.objects.filter(quantidade__in=[0])

    valorZerado= len(zerado)
    return render(request, "home.html", {'minimo': valorMinimo, 'critico': valorCritico,'zerado': valorZerado })
