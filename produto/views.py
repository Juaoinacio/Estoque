from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from produto.models import Produto, Categoria
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

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
            categoria = Categoria.objects.all()

            produtos = Produto.objects.all()
            
            # lista que ira guardar todos os meus produtos
            arrayEntradaGeral = []

            if produtos.exists(): # produtos existe ?
                
               for p in produtos: 
                    # abrimos um dicionário passando os atributos do Model "Produto".
                    dados = {
                        "importado" : p.importado,
                        "id" : p.id,
                        "nome" : p.nome, 
                        "ncm": p.ncm,
                        "categoria": p.categoria.nome,
                        "preco" : p.preco,
                        "estoqueAtual" : p.estoqueAtual,
                        "estoqueMinimo" : p.estoqueMinimo
                    }

                    # instancio o "ItemCompra" para usar seus atributos e buscar o ultimo 

                    arrayEntradaGeral.append(dados)
            context = {
                "produtos" : arrayEntradaGeral,
                "categorias": categoria,
            }

            return render(request, "produtos.html", context)
        # Metodo POST da minha url ""
        elif request.method == "POST":
            
            nome =  request.POST.get("nome", 0)
            ncm = request.POST.get("ncm", 0)
            preco =  request.POST.get("preco", 0)
            categoria =  request.POST.get("categoria", 0) # id que vem da minha categoria, assim sabemos qual categoria esse produto é.
            estoqueAtual = request.POST.get("estoqueAtual", 0)
            estoqueMinimo = request.POST.get("estoqueMinimo", 0)
            importado = request.POST.get("importado") == "on"

            #  Cria um novo objeto Produto com os dados recebidos do formulário
            produto = Produto(
                nome = nome,
                preco = preco,
                ncm = ncm,
                importado = importado,
                estoqueAtual = estoqueAtual, 
                estoqueMinimo = estoqueMinimo,
                categoria = Categoria.objects.get(id=categoria), # Busca a instância da Categoria correspondente ao ID enviado
            )
    
            produto.save()  # Guarda as informações de cima no bando de dados
            return HttpResponseRedirect(reverse('index_produto'))
        else:
            messages.error(request, str(e))
            print(e)
            return HttpResponseRedirect(reverse('index_produto'))
    except Exception as e:
        messages.error(request, str(e))
        print(e)
        return HttpResponseRedirect(reverse('index_produto'))

def delete(request):
    try:
        if request.method == "POST":
            id = request.POST.get("id")
            produto = get_object_or_404(Produto, id=id)
            produto.delete()
            return HttpResponseRedirect(reverse('index_produto'))
        else: 
            messages.error(request, str(e))
            print(e)
            return HttpResponseRedirect(reverse('index_produto'))
    except Exception as e:
        messages.error(request, str(e))
        print(e)
        return HttpResponseRedirect(reverse('index_produto'))
    
def show(request, id):
    try:
        if request.method == "GET":
            produto = get_object_or_404(Produto, id=id)
            return render(request, "produto_show.html", {"produto": produto})
        else:
            messages.error(request, str(e))
            print(e)
            return HttpResponseRedirect(reverse('show_produto'))
    except Exception as e:
        messages.error(request, str(e))
        print(e)
        return HttpResponseRedirect(reverse('show_produto'))
    
def edit(request):
    try:
        if request.method == "POST":
            produto = get_object_or_404(Produto, id=request.POST["id"])
            categoria = Categoria.objects.all()
            context = {
                "produto": produto,
                "categorias": categoria
            }
            return render(request, "produto_edit.html", context)
        else:
            messages.error(request, "Metodo não permitdo")
            return redirect(reverse("index_produto"))
    except Exception as e:
            messages.error(request, str(e))
            print(e)
            return HttpResponseRedirect(reverse('edit_produto'))

def save(request, id):
    try:
        if request.method == "POST":
            # Pega o id do produto
            id = request.POST.get("id")

            #Procura o produto no banco, caso de errado informa o erro 404
            produto = get_object_or_404(Produto, id=id)

            #Recebemos os atributos via POST
            nome =  request.POST.get("nome", 0)
            preco =  request.POST.get("preco", 0)
            ncm = request.POST.get("ncm", 0)
            importado = 'importado' in request.POST
            estoqueAtual = request.POST.get("estoqueAtual", 0)
            estoqueMinimo = request.POST.get("estoqueMinimo", 0)
            categoria = request.POST.get("categoria", 0)

            #Substituimos os Valores antigos pelos novos
        
            produto.nome = nome
            produto.preco = preco.replace(",", ".")
            produto.ncm = ncm
            produto.importado = importado
            produto.estoqueAtual = estoqueAtual 
            produto.estoqueMinimo = estoqueMinimo
            produto.categoria = Categoria.objects.get(id=categoria)

            #Salva os valores no banco
            produto.save()
            return redirect(reverse("index_produto"))
        else:
            messages.error(request, "Metodo não permitido")
            return redirect(reverse("show_produto", kwargs={"id": request.GET["id"]}))
    except Exception as e:
            messages.error(request, str(e))
            print(e)
            return redirect(reverse("show_produto", kwargs={"id": request.POST.get("id")}))
