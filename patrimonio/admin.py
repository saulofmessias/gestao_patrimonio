from django.contrib import admin
from django import forms
from import_export.admin import ImportExportModelAdmin
from .models import BemPatrimonial
from .resources import BensResource  # Se tiver


@admin.register(BemPatrimonial)
class BemAdmin(ImportExportModelAdmin):
    resource_class = BensResource  # Se existir, senão remove

    list_display = [
        'numero_patrimonio',
        'nome_patrimonio',
        'departamentos',
        'status',
        'localizacao_patrimonio',
        'categoria_patrimonio'
    ]

    list_filter = [
        'departamentos',
        'status',
        'categoria_patrimonio',
        'criado_em'
    ]

    search_fields = ['numero_patrimonio', 'nome_patrimonio', 'departamentos']

    list_per_page = 20
