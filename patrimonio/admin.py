# ARQUIVO: src/gestao_patrimonio/patrimonio/admin.py

from django.contrib import admin
from .models import BemPatrimonial, Categoria, Localizacao, Usuario

@admin.register(BemPatrimonial)
class BemPatrimonialAdmin(admin.ModelAdmin):
    # ✅ CORRIGIDO: list_display com campos que REALMENTE EXISTEM
    list_display = ['id', 'nome', 'status', 'categoria']
    
    # Filtros na lateral
    list_filter = ['status', 'categoria', 'data_criacao']
    
    # Busca rápida
    search_fields = ['nome', 'id']
    
    # Campos editáveis inline
    list_editable = ['status']
    
    # Paginação
    list_per_page = 50
    
    # Ordenação padrão
    ordering = ['-data_criacao']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'descricao']
    search_fields = ['nome']

@admin.register(Localizacao)
class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'cidade', 'estado']
    search_fields = ['nome', 'cidade']
    list_filter = ['estado', 'cidade']

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'funcao']
    search_fields = ['nome', 'email']
    list_filter = ['funcao']
