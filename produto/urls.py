from django.urls import path
from . import views

urlpatterns = [

#   |---------------------------- Crud dos produtos ----------------------|

    path("", views.index, name="produtos"),
    path("<int:id>/", views.produto_show, name="produto"),
    path("deletar_produto", views.deletar_produto, name="deletar_produto"),
    path('editar_produto/<int:id>/', views.editar_produto, name='editar_produto'),

#   |------------- Urls dos produto Minimo,Critico e Zerado. -------------|
   
]