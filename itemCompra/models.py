from django.db import models
from produto.models import Produto

class ItemCompra(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()
    precoUnitario = models.DecimalField(max_digits=10, decimal_places=2)

class Meta:
    db_table = "ItemCompra" 

def __str__(self):
    return f"Nome: {self.nome} "
