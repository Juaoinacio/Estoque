from django.db import models
from django.core.validators import RegexValidator

class Fornecedor(models.Model):
    nome = models.CharField(null=False, max_length=30)
    cnpj = models.CharField(max_length=60, unique=True, validators=[RegexValidator(regex='^\d+$', message='O código de barras deve conter apenas números.')], null=False)

    class Meta:
        db_table = 'Fornecedor'

    def __str__(self):
        return f"Fornecedor: {self.nome} CNPJ: {self.cnpj}"