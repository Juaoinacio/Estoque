from django.db import models

class TipoDePagamento(models.Model):
    nome = models.CharField(null=False, max_length=30)

    class Meta:
        db_table = "tipoDePagamento"

    def __str__(self):
        return f"{self.nome} "

