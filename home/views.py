from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from produto.models import Produto, Categoria
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

def index(request):
    return render(request, "home.html")