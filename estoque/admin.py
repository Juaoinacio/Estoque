from django.contrib import admin
from .models import Estoque, EstoqueItem

class EstoqueItensInLine(admin.TabularInline):
    model = EstoqueItem
    extra = 0

@admin.register(Estoque)
class EstoqueAdimin(admin.ModelAdmin):
    inlines = (EstoqueItensInLine, ) 
    list_display = (
        "__str__", "nf","funcionario",
    )
    search_fields = ("nf", )
    list_filter = ("funcionario", )
    date_hierarchy = "criado"




