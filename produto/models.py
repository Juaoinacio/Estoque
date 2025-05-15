from django.db import models
from categoria.models import Categoria
from datetime import datetime
from django.core.validators import RegexValidator

class Produto(models.Model):
    cod_barras = models.CharField(max_length=20, validators=[RegexValidator(regex='^\d+$', message='O código de barras deve conter apenas números.')], null=False)
    nome = models.CharField(max_length=50)
    quantidade = models.IntegerField(default=0)
    valorPago = models.DecimalField(null=False, max_digits=50,decimal_places=2)
    valorVenda = models.DecimalField(null=False, max_digits=50,decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    date = models.DateTimeField(default=datetime.now, blank=True)

    @property
    def status(self):
        if self.quantidade == 0:
            return "Zerado"
        elif self.quantidade < 100:
            return "Critico"
        elif self.quantidade < 200:
            return "Minimo"
        else:
            return "Normal"


    # Class Meta ser ver para aplicar regras na sua tabela
    class Meta:
        db_table = "Produto"

    def __str__(self):
        return f"Nome: {self.nome} - QTD: {self.quantidade} "

        