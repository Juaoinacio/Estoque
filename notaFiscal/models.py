from django.db import models
from compra.models import Compra
from venda.models import Venda

class NotaFiscal(models.Model):
    numero = models.BigIntegerField()
    valorTotal = models.BigIntegerField()
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "NotaFiscal"

    def __str__(self):
        return f"Nota Fiscal N°: {self.numero}"
    

    