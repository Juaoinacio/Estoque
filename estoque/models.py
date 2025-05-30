from django.db import models
from produto.models import Produto
from tipoDePagamento.models import TipoDePagamento
from core.models import CarimboData
from django.contrib.auth.models import User

Movimento = (
    ('E', 'Entrada'),
    ('S', 'Saida'),
)

class Estoque(CarimboData):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    nf = models.PositiveIntegerField(null=True, blank=True)
    movimento = models.CharField(max_length=1, choices=Movimento)
    tp = models.ForeignKey(TipoDePagamento, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-criado',) # Ordenar de forma decrescente
        db_table = "Estoque" 

    def __str__(self):
        return f"{self.pk}"

class EstoqueItem(models.Model):
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField()

    class Meta:
        ordering = ('pk',)
        db_table = "EstoqueItem" 
    
    def __str__(self):
        return f"{self.pk} Estoque ID:{self.estoque} {self.produto}" # PK referencia a primary key (chave primaria) == id
