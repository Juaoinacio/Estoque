from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from produto.models import Produto, Categoria
from compra.models import Compra, ItemCompra
from venda.models import Venda, ItemVenda
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import datetime
from django.db.models import Sum

data = datetime.now().month

def validar_codigo(codigo):
    validador = RegexValidator(regex='^\d+$', message='O código de barras deve conter apenas números.')
    try:
        validador(codigo)
        return True
    except ValidationError:
        return False


 # Tela inicial
def index(request):
    try:
        # Metodo GET da minha url ""
        if request.method == "GET":

            # Busco todos os produtos no banco de dados
            produtos = Produto.objects.all()

            # lista que ira guardar todos os meus produtos
            arrayEntradaGeral = []

            if produtos.exists(): # produtos existe ? 
               for p in produtos: 
                    # abrimos um dicionário passando os atributos do Model "Produto".
                    dados = {
                        "nome" : p.nome, 
                        "cod_barra" : p.cod_barras, 
                        "categoria": p.categoria.nome, 
                    }

                    # instancio o "ItemCompra" para usar seus atributos e buscar o ultimo 
                    item = ItemCompra.objects.filter(produto=p).order_by('-compra__date').first()
                   
                    if item is None:
                        dados["entrada"] = "N/D"
                        dados["preco"] = 0.00
                        dados["quantidade"] = 0
                        dados["status"] = "Zerado"
                    else:
                        ultimaCompra = item.compra # id da compra 
                        dados["entrada"] = ultimaCompra.date.strftime(("%d/%m/%Y, %H:%M:%S"))
                        totalValorCompra = item.precoUnitario * item.quantidade   
                        dados["preco"] = totalValorCompra
                        
                        # Soma total da quantidade de compras para este produto
                        somaQuantidade = ItemCompra.objects.filter(produto=p).aggregate(total=Sum('quantidade'))['total'] or 0
                        dados["quantidade"] = somaQuantidade

                         
    
                        if somaQuantidade < 100:
                            dados["status"] = "Critico"
                        elif somaQuantidade < 200:
                            dados["status"] = "Minimo"
                        else:
                            dados["status"] = "Normal"
                        
                        print(dados["status"])
                    itemv = ItemVenda.objects.filter(produto=p).last()
                    if itemv is None:
                        dados["saida"] = "N/D"
                    else:
                        ultimaVenda = itemv.venda # id da venda
                        dados["saida"] = ultimaVenda.date.strftime(("%d/%m/%Y, %H:%M:%S"))
                    
                    arrayEntradaGeral.append(dados)
                    

            context = {
                "produtos" : arrayEntradaGeral,
            }

            
            return render(request, "produtos.html", context)
        # Metodo POST da minha url ""
        elif request.method == "POST":
        
            # Anotação: cod_barras = Tabela do banco vazia (modelo Produto)
            (request.POST.get("cod_barras", 0)) # = O que eu recebo do Front-end caso eu deixo vazio

            cod_barras = request.POST.get("cod_barras", "")
            if validar_codigo(cod_barras) == False:
                messages.error(request, ("Apenas numeros"))
                return HttpResponseRedirect(reverse('produtos'))

            nome =  (request.POST.get("nome", 0))
            quantidade =  (request.POST.get("quantidade", 0))
            preco =  (request.POST.get("preco", 0))
            id_categoria =  (request.POST.get("id_categoria", 0)) # id que vem da minha categoria, assim sabemos qual categoria esse produto é.
            
            #  Cria um novo objeto Produto com os dados recebidos do formulário
            produto = Produto(
                cod_barras = cod_barras,
                nome = nome,
                quantidade = quantidade,
                preco = preco,
                categoria = Categoria.objects.get(id=id_categoria) # Busca a instância da Categoria correspondente ao ID enviado
            )
    
            produto.save()  # Guarda as informações de cima no bando de dados
            return HttpResponseRedirect(reverse('produtos'))
        
        else:
            messages.error(request, ("Método Http não permitido!"))
            return HttpResponseRedirect(reverse('produtos'))

    except Exception as e:
        messages.error(request, str(e))
        print(e)
        return HttpResponseRedirect(reverse('produtos'))

def deletar_produto(request):
    try:
        if request.method == "POST":
            id = request.POST.get("id")
            produto = get_object_or_404(Produto, id=id)
            produto.delete()
            return HttpResponseRedirect(reverse('produtos'))
        else: 
            messages.error(request, str(e))
            print(e)
            return HttpResponseRedirect(reverse('produtos'))
    except Exception as e:
        messages.error(request, str(e))
        print(e)
        return HttpResponseRedirect(reverse('produtos'))
    
def editar_produto(request):
    if request.method == "POST":
        # Pega o id do produto
        id = request.POST.get("id")

    #Procura o produto no banco, caso de errado informa o erro 404
        produto = get_object_or_404(Produto, id=id)

        #Recebemos os atributos via POST
        cod_barras =  (request.POST.get("cod_barras", 0))
        nome =  (request.POST.get("nome", 0))
        quantidade =  (request.POST.get("quantidade", 0))
        preco =  (request.POST.get("preco", 0))
        id_categoria =  (request.POST.get("id_categoria", 0))

        #Substituimos os Valores antigos pelos novos
        
        produto.cod_barras = cod_barras
        produto.nome = nome
        produto.quantidade = quantidade
        produto.preco = preco
        produto.categoria = Categoria.objects.get(id=id_categoria)

        #Salva os valores no banco
        produto.save()
        return HttpResponseRedirect(reverse('produtos'))
