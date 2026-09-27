from django.urls import path
from loja.views.ProdutoView import list_produto_view, edit_produto_view, edit_produto_postback, details_produto_view, delete_produto_view, delete_produto_postback, create_produto_view, adicionar_carrinho, carrinho_view, aumentar_quantidade, diminuir_quantidade, confirmar_compra
urlpatterns = [
     path("", list_produto_view, name= 'produto'),
     path("<int:id>", list_produto_view, name= 'produto'),

     path("edit/<int:id>", edit_produto_view, name= 'edit_produto'),
     path("edit", edit_produto_postback, name= 'edit_produto_postback'),

     path("details/<int:id>", details_produto_view, name= 'details_produto'),

     path("delete/<int:id>", delete_produto_view, name='delete_produto'),
     path("delete", delete_produto_postback, name='delete_produto_postback'),

     path("create", create_produto_view, name= 'create_produto'),
     
     path("carrinho/", carrinho_view, name="carrinho"),
     path("carrinho/adicionar/<int:id>/", adicionar_carrinho, name="adicionar_carrinho"),
     path("carrinho/aumentar/<int:id>/", aumentar_quantidade, name="aumentar_quantidade"),
     path("carrinho/diminuir/<int:id>/", diminuir_quantidade, name="diminuir_quantidade"),
     path("carrinho/confirmar/", confirmar_compra, name="confirmar_compra"),
]
