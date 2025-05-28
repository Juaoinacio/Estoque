from django.db import models
from produto.models import Produto

class Extoque(models.Model):
    produto = models.ForeignKey(Produto,on_delete=models.PROTECT)
    quantidade = models.IntegerField()

    class Meta:
        db_table = "Extoque" 

    def __str__(self):
        return f"Produto: {self.produto.nome}"


