from django.db import models
from produto.models import Produto

class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.BigIntegerField()

    class Meta:
        ordering = ('-criado',) # Ordenar de forma decrescente
        db_table = "Estoque" 

    def __str__(self):
        return f"{self.pk} - {self.criado.strftime("%d-%m-%Y")} - {self.nf}"