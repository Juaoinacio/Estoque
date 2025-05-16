from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime
from produto.models import Produto
from tipoDePagamento.models import TipoDePagamento 
from fornecedor.models import Fornecedor 

class Compra(models.Model):
    notaFiscal = models.CharField(max_length=60, validators=[RegexValidator(regex='^\d+$', message='O código de barras deve conter apenas números.')], null=False)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
    tipoDePagamento = models.ForeignKey(TipoDePagamento, on_delete=models.PROTECT)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date = models.DateTimeField(default=datetime.now, blank=True)
     
    class Meta:
        db_table = "Compra"

    def __str__(self):
        return f"Nome: {self.notaFiscal} "


class ItemCompra(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()
    precoUnitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "ItemCompra" 

    def __str__(self):
        return f"Nome: {self.produto.nome} "
