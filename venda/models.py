from django.db import models
from cliente.models import Cliente
from core.models import CarimboData
from produto.models import Produto
from tipoDePagamento.models import TipoDePagamento

class Venda(CarimboData):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipoDePagamento = models.ForeignKey(TipoDePagamento, on_delete=models.CASCADE)

    class Meta:
        db_table = "Venda"

    def __str__(self):
        return f"Nome: {self.cliente}"
    
class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.BigIntegerField()
    preco = models.FloatField()
    
    class Meta:
        db_table = "ItemVenda"

    def __str__(self):
        return f"Nome: {self.quantidade} - {self.preco}"
    



    