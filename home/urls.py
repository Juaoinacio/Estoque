from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("deletar_produto", views.deletar_produto, name="deletar_produto")
]
