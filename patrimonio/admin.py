from django.contrib import admin
from .models import Patrimonio  # Ajuste se model nome diferente

@admin.register(Patrimonio)
class PatrimonioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'secretaria', 'valor', 'data_aquisicao', 'status']
    list_filter = ['secretaria', 'status', 'data_aquisicao']
    search_fields = ['nome', 'descricao']
    list_editable = ['status']
    readonly_fields = ['criado_em']
    
    fieldsets = (
        ('Dados Básicos', {
            'fields': ('nome', 'secretaria', 'valor')
        }),
        ('Detalhes', {
            'fields': ('descricao', 'data_aquisicao', 'status', 'imagem')
        }),
        ('Automático', {
            'fields': ('criado_em',),
            'classes': ('collapse',)
        }),
    )
