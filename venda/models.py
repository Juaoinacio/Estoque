from django.db import models
from produto.models import Produto
from django.core.validators import RegexValidator
from tipoDePagamento.models import TipoDePagamento
from datetime import datetime

class Venda(models.Model):
    notaFiscal = models.CharField(max_length=60, validators=[RegexValidator(regex='^\d+$', message='O código de barras deve conter apenas números.')], null=False)
    tipoDePagamento = models.ForeignKey(TipoDePagamento, on_delete=models.PROTECT)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateTimeField(default=datetime.now, blank=True)
     
    class Meta:
        db_table = "Venda"

    def __str__(self):
        return f"Nome: {self.nome} "

class ItemVenda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()
    precoUnitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'ItemVenda'

    def __str__(self):
        return f"Nome: {self.nome}"
