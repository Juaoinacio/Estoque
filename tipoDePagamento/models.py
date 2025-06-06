from django.db import models

class TipoDePagamento(models.Model):
    tipo = models.CharField(null=False, max_length=30)

    class Meta:
        db_table = "TipoDePagamento"

    def __str__(self):
        return f"Tipo de pagamento: {self.tipo} "

