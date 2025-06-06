from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=12)
    cpe = models.CharField(max_length=8)
    
    class Meta:
        db_table = "Cliente"

    def __str__(self):
        return f"Nome: {self.nome}"

