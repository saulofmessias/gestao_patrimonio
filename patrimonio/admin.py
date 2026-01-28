from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import BemPatrimonial, CategoriaPatrimonio, Localizacao, Colaborador


@admin.register(BemPatrimonial)
class BemPatrimonialAdmin(ImportExportModelAdmin):
    list_display = ('numero_patrimonio', 'nome_patrimonio',
                    'localizacao', 'status', 'data_compra')  # CORRIGIDO
    list_filter = ('localizacao', 'status', 'data_compra',
                   'categoria')  # CORRIGIDO
    search_fields = ('numero_patrimonio', 'nome_patrimonio')  # CORRIGIDO
    ordering = ('numero_patrimonio',)  # CORRIGIDO

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('numero_patrimonio', 'nome_patrimonio', 'categoria', 'imagem')
        }),
        ('Valores e Datas', {
            'fields': ('quantidade', 'custo_compra', 'data_compra')
        }),
        ('Localização e Responsáveis', {
            'fields': ('localizacao', 'colaborador_responsavel')
        }),
        ('Status', {
            'fields': ('status',)
        }),
    )


@admin.register(CategoriaPatrimonio)
class CategoriaPatrimonioAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Localizacao)
class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'gerente')


@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'email', 'ativo')
