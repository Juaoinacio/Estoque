from compra.models import Compra
from venda.models import Venda
from .models import Produto

def anosMes(nMes, type):
    if type == "c":
        mes = len(Compra.objects.filter(date__month = nMes))
    else:
        mes = len(Venda.objects.filter(date__month = nMes))

    return mes
