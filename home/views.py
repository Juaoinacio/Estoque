from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse



def index(request):
    try:
        context = {   
        }
        return render(request, "home.html", context)
        
    except Exception as e:
        print(e)
        return HttpResponseRedirect(reverse('home'))
        
