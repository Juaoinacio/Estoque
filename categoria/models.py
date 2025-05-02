from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        db_table = "Categoria"

    def __str__(self):
        return f"Categoria: {self.nome}"
    