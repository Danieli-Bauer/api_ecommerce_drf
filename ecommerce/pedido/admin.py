from django.contrib import admin
from .models import Pedido, Item

# admin.site.register(Pedido, Item)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'descricao', 'get_criado_em', 'get_atualizado_em',)
    list_filter = ('cliente',)
    search_fields = ['id', 'cliente__nome', 'cliente__cpf', 'descricao',]
    list_display_links = ('cliente',)
    
    def get_criado_em(self, obj):
        if obj.criado_em:
            return obj.criado_em.strftime('%d/%m/%Y')
    
    get_criado_em.short_description = 'Criado em'
    
    def get_atualizado_em(self, obj):
        if obj.atualizado_em:
            return obj.atualizado_em.strftime('%d/%m/%Y')
    
    get_atualizado_em.short_description = 'Atualizado em'
    
    
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'pedido', 'produto', 'quantidade', 'get_criado_em', 'get_atualizado_em',)
    list_filter = ('pedido', 'produto',)
    search_fields = ['pedido__id', 'pedido__descricao', 'produto__nome',]
    list_display_links = ('pedido', 'produto',)
    
    def get_criado_em(self, obj):
        if obj.criado_em:
            return obj.criado_em.strftime('%d/%m/%Y')
    
    get_criado_em.short_description = 'Criado em'
    
    def get_atualizado_em(self, obj):
        if obj.atualizado_em:
            return obj.atualizado_em.strftime('%d/%m/%Y')
    
    get_atualizado_em.short_description = 'Atualizado em'
    
    