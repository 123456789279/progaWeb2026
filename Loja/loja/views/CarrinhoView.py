from django.shortcuts import render, get_object_or_404, redirect
from loja.models import Produto, Carrinho, CarrinhoItem, Usuario
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def create_carrinhoitem_view(request, produto_id=None):
    produto = get_object_or_404(Produto, pk=produto_id)
    carrinho_id = request.session.get('carrinho_id')
    carrinho = None
    if carrinho_id:
        carrinho = Carrinho.objects.filter(id=carrinho_id).first()
        if carrinho is None or carrinho.criado_em.date() != datetime.today().date():
            carrinho = Carrinho.objects.create()
            request.session['carrinho_id'] = carrinho.id
    else:
        carrinho = Carrinho.objects.create()
        request.session['carrinho_id'] = carrinho.id
    carrinho_item = CarrinhoItem.objects.filter(
        carrinho=carrinho,
        produto=produto
    ).first()
    if carrinho_item:
        carrinho_item.quantidade += 1
    else:
        carrinho_item = CarrinhoItem.objects.create(
            carrinho=carrinho,
            produto=produto,
            quantidade=1,
            preco=produto.preco
        )
    carrinho_item.save()
    return redirect('/carrinho/')


def list_carrinho_view(request):
    carrinho = None
    itens = []
    carrinho_id = request.session.get('carrinho_id')
    if carrinho_id:
        carrinho = Carrinho.objects.filter(id=carrinho_id).first()

        if carrinho:
            itens = CarrinhoItem.objects.filter(carrinho=carrinho)
    context = {
        'carrinho': carrinho,
        'itens': itens
    }
    return render(
        request,
        'carrinho/carrinho-listar.html',
        context=context
    )

def aumentar_quantidade_view(request, item_id):
    item = get_object_or_404(CarrinhoItem, id=item_id)
    carrinho_id = request.session.get('carrinho_id')
    if carrinho_id == item.carrinho.id:
        item.quantidade += 1
        item.save()
    return redirect('/carrinho/')

def diminuir_quantidade_view(request, item_id):
    item = get_object_or_404(CarrinhoItem, id=item_id)
    carrinho_id = request.session.get('carrinho_id')
    if carrinho_id == item.carrinho.id:
        if item.quantidade > 1:
            item.quantidade -= 1
            item.save()
        else:
            item.delete()
    return redirect('/carrinho/')

@login_required
def confirmar_carrinho_view(request):
    carrinho = None
    carrinho_id = request.session.get('carrinho_id')
    if carrinho_id:
        carrinho = Carrinho.objects.filter(id=carrinho_id).first()
        if carrinho:
            usuario = get_object_or_404(
                Usuario,
                user=request.user
            )
            carrinho.user_id = usuario.id
            carrinho.situacao = 1
            carrinho.confirmado_em = timezone.now()
            carrinho.save()
    context = {
        'carrinho': carrinho
    }
    return render(
        request,
        'carrinho/carrinho-confirmado.html',
        context=context
    )

def remover_item_view(request, item_id):
    item = get_object_or_404(CarrinhoItem, id=item_id)
    carrinho_id = request.session.get('carrinho_id')
    if carrinho_id == item.carrinho.id:
        item.delete()
    return redirect('/carrinho/')
