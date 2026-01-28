from django.contrib import admin
from .models import BemPatrimonial
from import_export.admin import ImportExportModelAdmin

@admin.register(BemPatrimonial)
class BemPatrimonialAdmin(ImportExportModelAdmin):
    list_display = ('numero_tombo', 'nome_patrimonio', 'secretaria', 'status', 'data_compra')
    list_filter = ('secretaria', 'status', 'data_compra')
    search_fields = ('numero_tombo', 'nome_patrimonio', 'departamento')
    ordering = ('numero_tombo',)
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('numero_tombo', 'nome_patrimonio', 'numero_nf', 'descricao', 'tipo')
        }),
        ('Valores e Datas', {
            'fields': ('quantidade', 'valor', 'data_compra')
        }),
        ('Localização e Responsáveis', {
            'fields': ('secretaria', 'departamento', 'localizacao', 'gerente_responsavel')
        }),
        ('Status e Mídia', {
            'fields': ('status', 'imagem')
        }),
    )
