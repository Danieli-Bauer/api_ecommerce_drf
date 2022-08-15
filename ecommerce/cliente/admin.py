from django.contrib import admin
from .models import Cliente

# admin.site.register(Cliente)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone','email', 'endereco', 'get_criado_em', 'get_atualizado_em')
    list_filter = ('nome', 'cpf', 'telefone')
    search_fields = ('nome', 'cpf', 'endereco','email')
    
    def get_criado_em(self, obj):
        if obj.criado_em:
            return obj.criado_em.strftime('%d/%m/%Y')
    
    get_criado_em.short_description = 'Criado em'
    
    def get_atualizado_em(self, obj):
        if obj.criado_em:
            return obj.criado_em.strftime('%d/%m/%Y')
    
    get_atualizado_em.short_description = 'Atualizado em'
    
    