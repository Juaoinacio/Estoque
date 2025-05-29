from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "importado",
        "ncm",
        "nome",
        "estoqueAtual",
        "estoqueMinimo",
        "preco",
        "categoria",
    )
    list_filter = ("categoria","importado", )
    search_fields = ("categoria",)
    