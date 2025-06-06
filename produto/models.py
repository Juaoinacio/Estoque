from django.db import models
from categoria.models import Categoria
from django.core.validators import RegexValidator

class Produto(models.Model):
    importado = models.BooleanField(default=False)
    nome = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    # Class Meta ser ver para aplicar regras na sua tabela
    class Meta:
        ordering = ('nome',)
        db_table = "Produto"

    def __str__(self):
        return f"Nome: {self.nome}"