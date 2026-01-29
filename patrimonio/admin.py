from django.contrib import admin
from .models import BemPatrimonial, CategoriaPatrimonio, Localizacao, Colaborador

@admin.register(BemPatrimonial)
class BemPatrimonialAdmin(admin.ModelAdmin):
    list_display = ['numero_patrimonio', 'nome_patrimonio', 'status', 'categoria', 'localizacao']
    list_filter = ['status', 'categoria', 'criado_em']
    search_fields = ['nome_patrimonio', 'numero_patrimonio']
    list_editable = ['status']
    list_per_page = 50
    ordering = ['-criado_em']

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
