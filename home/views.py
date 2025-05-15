from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from produto.util_prod import statusMinimo, statusCritico, statusZerado, entradaMes


def index(request):
    entradaMes()
    try:
        context = {   
            'minimo': statusMinimo(), 
            'critico': statusCritico(),
            'zerado': statusZerado(),
#            'entrada': , 
        }
        return render(request, "home.html", context)
        
    except Exception as e:
        print(e)
        return HttpResponseRedirect(reverse('home'))
        
