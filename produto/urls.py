from django.urls import path
from . import views

urlpatterns = [

#   |---------------------------- Crud dos produtos ----------------------|

    path("", views.index, name="index_produto"),
    path("<int:id>/", views.show, name="show_produto"),
    path("deletar_produto", views.delete, name="delete_produto"),
    path('edit_show_produto/', views.edit, name='edit_produto'),
    path('salvar_produto/<int:id>', views.save, name='save_produto'),
   
]