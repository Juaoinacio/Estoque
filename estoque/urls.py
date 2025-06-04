from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index_estoque_entrada"),
    path("itemEntrada/", views.add , name="add_estoque_entrada"),
    path("<int:id>", views.show, name="show_estoque_entrada"),
]
