from .models import Produto
from datetime import date
from django.db.models import Sum

#|------ Funções que retornam a contidade de cada status dos produtos -----|

def statusMinimo():
    return len(Produto.objects.filter(quantidade__range=[101, 200])) 
def statusCritico():
    return len(Produto.objects.filter(quantidade__range=[1, 100]))
def statusZerado():
    return len(Produto.objects.filter(quantidade = 0))

#|---------------------------------- END ----------------------------------|
