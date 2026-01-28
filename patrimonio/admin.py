from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html
from .models import *


@admin.register(BemPatrimonial)
class BemPatrimonialAdmin(ImportExportModelAdmin):
    list_display = ['numero_patrimonio', 'nome_patrimonio',
                    'status_badge', 'localizacao', 'custo_compra']
    list_filter = ['status', 'categoria', 'localizacao', 'data_compra']
    search_fields = ['numero_patrimonio', 'nome_patrimonio']
    list_per_page = 25

    def status_badge(self, obj):
        colors = {
            'disponivel': 'success',
            'alocado': 'warning',
            'manutencao': 'info',
            'descartado': 'danger'
        }
        return format_html('<span class="badge badge-{}">{}</span>',
                           colors.get(obj.status, 'secondary'), obj.get_status_display())
    status_badge.short_description = 'Status'


@admin.register(CategoriaPatrimonio)
class CategoriaPatrimonioAdmin(admin.ModelAdmin):
    list_display = ['nome']


@admin.register(Localizacao)
class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ['nome']


@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ['nome_completo', 'email', 'ativo']
