# ARQUIVO: src/patrimonio/admin.py

from django.contrib import admin
from .models import BemPatrimonial, CategoriaPatrimonio, Localizacao, Colaborador

@admin.register(BemPatrimonial)
class BemPatrimonialAdmin(admin.ModelAdmin):
    # ✅ CORRIGIDO: list_display com campos que REALMENTE EXISTEM
    list_display = ['numero_patrimonio', 'nome_patrimonio', 'status', 'categoria', 'localizacao']
    
    # Filtros na lateral
    list_filter = ['status', 'categoria', 'criado_em']
    
    # Busca rápida
    search_fields = ['nome_patrimonio', 'numero_patrimonio']
    
    # Campos editáveis inline
    list_editable = ['status']
    
    # Paginação
    list_per_page = 50
    
    # Ordenação padrão
    ordering = ['-criado_em']
    
    # Grupos de campos no formulário
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('numero_patrimonio', 'nome_patrimonio', 'quantidade')
        }),
        ('Classificação', {
            'fields': ('categoria', 'status')
        }),
        ('Localização e Responsável', {
            'fields': ('localizacao', 'colaborador_responsavel')
        }),
        ('Dados Financeiros', {
            'fields': ('custo_compra', 'data_compra')
        }),
        ('Imagem', {
            'fields': ('imagem',)
        }),
    )

@admin.register(CategoriaPatrimonio)
class CategoriaPatrimonioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'descricao']
    search_fields = ['nome']

@admin.register(Localizacao)
class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'cidade', 'gerente']
    search_fields = ['nome', 'cidade']
    list_filter = ['cidade']

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_completo', 'email', 'funcao', 'ativo']
    search_fields = ['nome_completo', 'email']
    list_filter = ['funcao', 'ativo']
    list_editable = ['ativo']
