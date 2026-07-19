from django.shortcuts import render
from loja.models import Produto
from loja.models import Categoria
def home_view(request):
    produto = request.GET.get("produto")
    produtos = Produto.objects.all()
    if produto is not None:
        produtos = produtos.filter(Produto__contains=produto)

    categoria = request.GET.get("produto")
    categorias = Categoria.objects.all()
    if categoria is not None:
        categorias = categorias.filter(Categoria__contains=categoria)
    
    context = {
        'produtos': produtos
        'categorias': categorias
    }
    return render(request, template_name='home/home.html', context=context, status=200)
