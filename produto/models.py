from django.db import models


class Produto(models.Model):
    cod_barras = models.IntegerField(null=False)
    nome = models.CharField(max_length=50)
    quantidade = models.IntegerField(default=0)
    preco = models.DecimalField(null=False)

