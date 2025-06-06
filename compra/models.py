from core.models import CarimboData
from django.db import models
from fornecedor.models import Fornecedor
from notaFiscal.models import NotaFiscal
from tipoDePagamento.models import TipoDePagamento
class Compra(CarimboData):
    notaFiscal = models.ForeignKey(NotaFiscal, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    tipoDePagamento = models.ForeignKey(TipoDePagamento, on_delete=models.CASCADE)
    