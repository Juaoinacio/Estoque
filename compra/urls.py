from django.urls import path
from . import views

urlpatterns = [

#   |---------------------------- Crud dos produtos ----------------------|
    path("", views.index, name="comprar"),
    path("itemCompra", views.itemCompra, name="itemCompra"),
    path("editarItemCompra", views.editarItemCompra, name="editarItemCompra"),


]
