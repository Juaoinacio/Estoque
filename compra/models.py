from core.models import CarimboData
from django.db import models
from fornecedor.models import Fornecedor
from produto.models import Produto
from tipoDePagamento.models import TipoDePagamento

class Compra(CarimboData):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    tipoDePagamento = models.ForeignKey(TipoDePagamento, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "Compra"

    def __str__(self):
        return f"Nota Fiscal N°:{self.fornecedor}"
    
class ItemCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.BigIntegerField()
    preco = models.FloatField()
    
    class Meta:
        db_table = "ItemCompra"

    def __str__(self):
        return f"Nome: {self.quantidade} - {self.preco}"
    
