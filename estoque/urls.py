from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index_estoque"),
    path("<int:id>", views.show,name="show_estoque"),
]
