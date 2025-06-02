from django.urls import path
from . import views

urlpatterns = [

#   |---------------------------- Crud dos produtos ----------------------|

    path("", views.index, name="produtos"),
    path("<int:id>/", views.produto_show, name="produto"),
    path("deletar_produto", views.deletar_produto, name="deletar_produto"),
    path('edit_show_produto/', views.edit_show_produto, name='edit_show_produto'),
    path('salvar_produto/<int:id>', views.salvar_produto, name='salvar_produto'),
   
]