from .models import Produto

def statusMinimo():
    return len(Produto.objects.filter(quantidade__range=[100, 200])) 

def statusCritico():
    critico = Produto.objects.filter(quantidade__range=[1, 100])

    valorCritico = len(critico)
    return valorCritico

def statusZerado():
    zerado = Produto.objects.filter(quantidade = 0)

    valorZerado= len(zerado)
    return valorZerado