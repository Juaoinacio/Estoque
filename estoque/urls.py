from django.urls import path
from . import views

urlpatterns = [
    path("", views.entrada, name="entrada"),
    path("<int:id>", views.detalhe_entrada,name="detalhe_entrada"),
]
