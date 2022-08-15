from django.contrib import admin
from .models import Produto

# admin.site.register(Produto)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao','preco', 'quantidade', 'get_criado_em', 'get_atualizado_em',)
    list_filter = ('nome', 'preco',)
    search_fields = ('nome', 'descricao', 'preco',)
    list_display_links = ('nome',)
    
    def get_criado_em(self, obj):
        if obj.criado_em:
            return obj.criado_em.strftime('%d/%m/%Y')
    
    get_criado_em.short_description = 'Criado em'
    
    def get_atualizado_em(self, obj):
        if obj.criado_em:
            return obj.criado_em.strftime('%d/%m/%Y')
    
    get_atualizado_em.short_description = 'Atualizado em'
    
    