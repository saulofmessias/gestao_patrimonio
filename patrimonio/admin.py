from django.contrib import admin
from .models import BemPatrimonial, CategoriaPatrimonio, Localizacao, Colaborador

class BemPatrimonialAdmin(admin.ModelAdmin):
    # Formulário mais simples, campos opcionais
    fields = ['numero_patrimonio', 'nome_patrimonio', 'imagem', 'quantidade', 'categoria', 
              'custo_compra', 'data_compra', 'localizacao', 'colaborador_responsavel', 'status']
    list_display = ['numero_patrimonio', 'nome_patrimonio', 'status']
    list_filter = ['status', 'categoria', 'criado_em']
    search_fields = ['nome_patrimonio', 'numero_patrimonio']
    list_editable = ['status']

@admin.register(CategoriaPatrimonio)
class CategoriaPatrimonioAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Localizacao)
class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cidade']

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ['nome_completo', 'email', 'ativo']

admin.site.register(BemPatrimonial, BemPatrimonialAdmin)
