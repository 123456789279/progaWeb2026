from django.contrib import admin

# Register your models here.
from .models import * #imporata nossos models
class FabricanteAdmin(admin.ModelAdmin):
    # Cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'
    fields = ('Produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria',)
    search_fields = ('Produto',)
class ProdutoAdmin(admin.ModelAdmin):
    # Cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria',)
    empty_value_display = 'Vazio'
    fields = ('Produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria',)
    search_fields = ('Produto',)
admin.site.register(Fabricante,FabricanteAdmin) #adiciona a interface do admim
admin.site.register(Categoria) #adiciona a interface do admim
admin.site.register(Produto, ProdutoAdmin) #adiciona a interface do admim
# incluir a tabela de usuário no final
admin.site.register(Usuario)
