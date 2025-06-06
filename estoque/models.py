from django.db import models
from produto.models import Produto

class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.BigIntegerField()

    class Meta:
        db_table = "Estoque" 

    def __str__(self):
        return f"Nome: {self.produto.nome} - QTD: {self.quantidade}"