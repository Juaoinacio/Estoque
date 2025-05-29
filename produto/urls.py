from django.urls import path
from . import views

urlpatterns = [

#   |---------------------------- Crud dos produtos ----------------------|

    path("", views.index, name="produtos"),
    path("deletar_produto", views.deletar_produto, name="deletar_produto"),
    path("editar_produto", views.editar_produto, name="editar_produto"),
    

#   |------------- Urls dos produto Minimo,Critico e Zerado. -------------|
   
]