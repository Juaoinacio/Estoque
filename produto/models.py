from django.db import models
from categoria.models import Categoria
from datetime import datetime

class Produto(models.Model):
    cod_barras = models.IntegerField(null=False)
    nome = models.CharField(max_length=50)
    quantidade = models.IntegerField(default=0)
    preco = models.DecimalField(null=False, max_digits=50,decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    date = models.DateTimeField(default=datetime.now, blank=True)

    # Class Meta ser ver para aplicar regras na sua tabela
    class Meta:
        db_table = "Produto"

    def __str__(self):
        return f"Nome: {self.nome} - QTD: {self.quantidade} "

        